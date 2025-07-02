<template>
  <div
    class="capture-face min-h-screen bg-gray-50 flex flex-col items-center justify-center px-4 py-8"
  >
    <!-- Navbar passo -->
    <nav class="fixed top-0 w-full bg-white shadow-md z-50">
      <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center">
          <router-link to="/" class="flex items-center">
            <div class="w-10 h-10 rounded-full bg-purple-700 flex items-center justify-center">
              <div class="w-6 h-6 rounded-full bg-orange-500"></div>
            </div>
            <span class="ml-3 text-xl font-bold text-purple-900">AFRICEL</span>
          </router-link>
        </div>
        <div>
          <span class="text-purple-700 font-medium">Passo 3 de 4</span>
        </div>
      </div>
    </nav>

    <!-- Título -->
    <div class="mt-20 text-center mb-6">
      <h1 class="text-3xl font-bold text-purple-900">Captura Facial</h1>
      <p class="text-gray-700 mt-2">Posicione-se em frente à câmera e capture sua foto</p>
      <div class="h-1 w-20 bg-orange-500 mx-auto mt-4"></div>
    </div>

    <!-- Preview e Canvas -->
    <div class="bg-white rounded-xl shadow-md p-6 w-full max-w-md">
      <div class="relative">
        <!-- Exibe vídeo apenas quando não há captura -->
        <video
          v-show="!captured"
          ref="video"
          class="w-full h-64 bg-black rounded-md object-cover"
          autoplay
          muted
          playsinline
        ></video>

        <!-- Exibe imagem capturada -->
        <div v-if="captured" class="w-full h-64 rounded-md overflow-hidden">
          <img :src="capturedImage" class="w-full h-full object-cover" alt="Foto capturada" />
        </div>

        <!-- Overlay de orientação -->
        <div v-show="!captured" class="absolute inset-0 flex items-center justify-center">
          <div class="border-2 border-white border-dashed rounded-full w-48 h-48"></div>
        </div>
      </div>

      <!-- Controles -->
      <div class="flex justify-center space-x-4 mt-6">
        <button
          v-if="!captured"
          @click="capture"
          class="btn-primary px-6 py-2 font-semibold rounded-full"
        >
          Capturar
        </button>
        <button
          v-if="captured"
          @click="retry"
          class="bg-gray-300 text-gray-700 px-6 py-2 rounded-full font-medium hover:bg-gray-400 transition"
        >
          Tentar Novamente
        </button>
        <button
          v-if="captured"
          @click="confirmAndSend"
          class="bg-purple-700 text-white px-6 py-2 rounded-full font-bold hover:bg-purple-800 transition disabled:opacity-70"
          :disabled="sending"
        >
          {{ sending ? 'Processando...' : 'Confirmar e Enviar' }}
        </button>
      </div>

      <!-- Feedback -->
      <div v-if="feedback" class="mt-4 text-center">
        <p :class="feedbackClass" class="font-semibold">
          <font-awesome-icon
            :icon="feedback === 'match' ? 'check-circle' : 'exclamation-circle'"
            class="mr-2"
          />
          {{ feedbackMessage }}
        </p>
        <button
          v-if="feedback === 'no-match'"
          @click="retry"
          class="mt-2 text-purple-700 font-semibold hover:underline"
        >
          Tentar novamente
        </button>
      </div>

      <!-- Dicas -->
      <div v-if="!captured" class="mt-6 text-sm text-gray-600 bg-purple-50 p-3 rounded-lg">
        <p class="font-semibold mb-1">Dicas para uma boa captura:</p>
        <ul class="list-disc pl-5 space-y-1">
          <li>Posicione-se em um ambiente bem iluminado</li>
          <li>Mantenha o rosto dentro do círculo</li>
          <li>Remova óculos escuros e bonés</li>
          <li>Mantenha uma expressão neutra</li>
        </ul>
      </div>
      <div class="fixed bottom-4 left-4">
        <button
          @click="voltarParaCapturaFacial"
          class="bg-gray-300 text-gray-700 px-4 py-2 rounded-full font-medium hover:bg-gray-400 transition flex items-center"
        >
          <font-awesome-icon icon="arrow-left" class="mr-2" /> Voltar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CapturePhoto',
  data() {
    return {
      stream: null,
      captured: false,
      capturedImage: null,
      sending: false,
      feedback: null, // 'match' or 'no-match'
    }
  },
  computed: {
    feedbackMessage() {
      if (this.feedback === 'match') return 'Rosto correspondente! Prosseguindo para validação...'
      if (this.feedback === 'no-match')
        return 'Rosto não corresponde ao documento. Tente novamente.'
      return ''
    },
    feedbackClass() {
      return {
        'text-green-600': this.feedback === 'match',
        'text-red-600': this.feedback === 'no-match',
        'flex items-center justify-center': true,
      }
    },
  },
  mounted() {
    this.startCamera()
  },
  beforeUnmount() {
    this.stopCamera()
  },
  methods: {
    async startCamera() {
      try {
        this.stream = await navigator.mediaDevices.getUserMedia({
          video: {
            facingMode: 'user',
            width: { ideal: 1280 },
            height: { ideal: 720 },
          },
        })
        this.$refs.video.srcObject = this.stream
      } catch (err) {
        console.error('Erro ao acessar câmera:', err)
        alert('Não foi possível acessar a câmera. Por favor, verifique as permissões.')
      }
    },

    stopCamera() {
      if (this.stream) {
        this.stream.getTracks().forEach((track) => track.stop())
        this.stream = null
      }
    },

    capture() {
      const video = this.$refs.video
      const canvas = document.createElement('canvas')
      const context = canvas.getContext('2d')

      // Configura canvas com proporções do vídeo
      canvas.width = video.videoWidth
      canvas.height = video.videoHeight

      // Desenha frame atual no canvas
      context.drawImage(video, 0, 0, canvas.width, canvas.height)

      // Converte para data URL (formato base64)
      this.capturedImage = canvas.toDataURL('image/jpeg', 0.9)
      this.captured = true

      // Para a câmera para economizar recursos
      this.stopCamera()
    },

    retry() {
      this.captured = false
      this.capturedImage = null
      this.feedback = null
      this.startCamera()
    },

    async confirmAndSend() {
      this.sending = true
      this.feedback = null

      try {
        // Simulação de chamada à API de reconhecimento facial
        // Na implementação real, enviaríamos this.capturedImage para o backend
        const isMatch = await this.compareFaces()

        if (isMatch) {
          this.feedback = 'match'

          // Simulação do registro da pessoa
          await this.registerUser()

          // Redireciona após breve delay para mostrar feedback
          setTimeout(() => {
            this.$router.push('/validate-sms')
          }, 1500)
        } else {
          this.feedback = 'no-match'
        }
      } catch (error) {
        console.error('Erro na verificação facial:', error)
        this.feedback = 'no-match'
      } finally {
        this.sending = false
      }
    },

    voltarParaCapturaFacial() {
      this.$router.push('/confirm-data')
    },

    // Simulação de comparação facial com o backend
    async compareFaces() {
      // Em produção, seria uma chamada API real:
      // return await axios.post('/api/face-match', { image: this.capturedImage })

      // Simulação com 80% de chance de sucesso
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve(Math.random() > 0.2) // 80% de match
        }, 1200)
      })
    },

    // Simulação de registro do usuário
    async registerUser() {
      // Em produção, enviaríamos todos os dados coletados nos passos anteriores
      return new Promise((resolve) => {
        setTimeout(() => {
          console.log('Usuário registrado com sucesso!')
          resolve()
        }, 500)
      })
    },
  },
}
</script>

<style scoped>
.btn-primary {
  background: linear-gradient(90deg, #f37021 0%, #662d91 100%);
  color: white;
  transition: all 0.3s ease;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(102, 45, 145, 0.25);
}

.capture-face {
  background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%);
}
</style>
