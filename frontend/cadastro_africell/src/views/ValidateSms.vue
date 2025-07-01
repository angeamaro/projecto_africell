<template>
  <div>
    <nav class="fixed w-full z-50 bg-white shadow-md">
      <div class="container mx-auto px-4 py-3">
        <div class="flex justify-between items-center">
          <div class="flex items-center">
            <div class="flex items-center">
              <div class="w-10 h-10 rounded-full bg-purple-700 flex items-center justify-center">
                <div class="w-6 h-6 rounded-full bg-orange-500"></div>
              </div>
              <router-link to="/" class="ml-3 text-xl font-bold text-purple-900 hover:underline">
                AFRICEL
              </router-link>
            </div>
          </div>

          <div class="flex items-center">
            <span class="text-purple-700 font-medium">Passo 4 de 5</span>
          </div>
        </div>
      </div>
    </nav>
    <main>
      <div class="min-h-screen bg-gray-50 flex items-center justify-center px-4">
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-md p-8">
          <div class="text-center mb-6">
            <div
              class="w-16 h-16 rounded-full bg-purple-100 flex items-center justify-center mx-auto mb-4"
            >
              <font-awesome-icon icon="sms" class="text-purple-700 text-2xl" />
            </div>
            <h2 class="text-2xl font-bold text-purple-900">Verificação de Telefone</h2>
            <p class="text-gray-600 mt-2">Insira o número para receber o código</p>
          </div>

          <form @submit.prevent="handleValidation" class="space-y-5">
            <!-- Número de Telefone -->
            <div>
              <label class="block text-gray-700 mb-1">Número de Telefone</label>
              <input
                v-model="phone"
                type="tel"
                placeholder="ex: 923123456"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
              />
            </div>

            <button
              type="button"
              @click="sendCode"
              class="btn-primary w-full py-3 text-white rounded-lg font-semibold"
            >
              Enviar Código
            </button>

            <!-- Campo do Código -->
            <div v-if="codeSent" class="pt-4">
              <label class="block text-gray-700 mb-1">Código Recebido</label>
              <input
                v-model="code"
                type="text"
                placeholder="Digite o código SMS"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
              />
            </div>

            <button
              v-if="codeSent"
              type="submit"
              class="w-full mt-4 py-3 bg-purple-700 text-white font-bold rounded-lg hover:bg-purple-800 transition"
            >
              Validar e Finalizar Cadastro
            </button>

            <!-- Feedback -->
            <div v-if="status" class="mt-4 text-center">
              <p
                :class="{
                  'text-green-600': status === 'válido',
                  'text-red-600': status === 'inválido' || status === 'expirado',
                }"
                class="font-semibold"
              >
                Código {{ status }}
              </p>
            </div>
          </form>
          <div class="flex flex-col sm:flex-row justify-between gap-4" style="margin-top: 20px">
            <button
              @click="voltarParaUpload"
              class="bg-gray-300 text-gray-700 px-6 py-3 rounded-full font-medium hover:bg-gray-400 transition"
            >
              <font-awesome-icon icon="arrow-left" class="mr-2" /> Voltar
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'VerifySMS',
  data() {
    return {
      phone: '',
      code: '',
      codeSent: false,
      status: '', // 'válido', 'inválido', 'expirado'
    }
  },
  methods: {
    sendCode() {
      if (this.phone.trim().length < 9) {
        alert('Número inválido.')
        return
      }
      this.codeSent = true
      this.status = ''
      // Simula envio de código SMS (em produção, você usaria uma API real)
      console.log(`Enviando código para: ${this.phone}`)
    },
    voltarParaUpload() {
      this.$router.push('/confirm-data')
    },
    handleValidation() {
      // Simula validação
      if (this.code === '1234') {
        this.status = 'válido'
        setTimeout(() => this.$router.push('/upload-bi'), 1500)
      } else if (this.code === '') {
        this.status = 'inválido'
      } else {
        this.status = 'expirado'
      }
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
