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
          <span class="text-purple-700 font-medium">Passo 3 de 5</span>
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
        <video
          ref="video"
          class="w-full h-64 bg-black rounded-md"
          autoplay
          muted
          playsinline
        ></video>
        <canvas
          v-if="captured"
          ref="canvas"
          class="absolute top-0 left-0 w-full h-64 rounded-md"
        ></canvas>
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
          Confirmar e Enviar
        </button>
      </div>

      <!-- Feedback -->
      <div v-if="feedback" class="mt-4 text-center">
        <p :class="feedbackClass" class="font-semibold">
          {{ feedbackMessage }}
        </p>
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
      sending: false,
      feedback: null, // 'match' or 'no-match'
    }
  },
  computed: {
    feedbackMessage() {
      if (this.feedback === 'match') return 'Rosto correspondente'
      if (this.feedback === 'no-match') return 'Rosto não correspondente'
      return ''
    },
    feedbackClass() {
      return {
        'text-green-600': this.feedback === 'match',
        'text-red-600': this.feedback === 'no-match',
      }
    },
  },
  mounted() {
    this.startCamera()
  },
  beforeUnmount() {
    if (this.stream) {
      this.stream.getTracks().forEach((track) => track.stop())
    }
  },
  methods: {
    async startCamera() {
      try {
        this.stream = await navigator.mediaDevices.getUserMedia({ video: true })
        this.$refs.video.srcObject = this.stream
      } catch (err) {
        console.error('Erro ao acessar câmera:', err)
      }
    },
    capture() {
      const video = this.$refs.video
      const canvas = this.$refs.canvas
      const context = canvas.getContext('2d')
      canvas.width = video.videoWidth
      canvas.height = video.videoHeight
      context.drawImage(video, 0, 0)
      this.captured = true
    },
    retry() {
      this.captured = false
      this.feedback = null
    },
    async confirmAndSend() {
      this.sending = true
      // Simula comparação facial
      setTimeout(() => {
        // Aleatoriamente simula match ou no-match
        this.feedback = Math.random() > 0.5 ? 'match' : 'no-match'
        this.sending = false
        if (this.feedback === 'match') {
          this.$router.push('/complete')
        }
      }, 1500)
    },
  },
}
</script>

<style scoped>
.btn-primary {
  background: linear-gradient(90deg, #f37021 0%, #662d91 100%);
  transition: all 0.3s ease;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(102, 45, 145, 0.25);
}
</style>
