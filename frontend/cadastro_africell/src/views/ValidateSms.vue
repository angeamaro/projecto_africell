<template>
  <div class="min-h-screen bg-gray-50 flex flex-col">
    <!-- Navbar passo -->
    <nav class="fixed top-0 w-full bg-white shadow-md z-50">
      <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center">
          <router-link to="/" class="flex items-center">
            <div class="w-10 h-10 rounded-full bg-purple-700 flex items-center justify-center">
              <div class="w-6 h-6 rounded-full bg-orange-500"></div>
            </div>
            <span class="ml-3 text-xl font-bold text-purple-900">AFRICELL</span>
          </router-link>
        </div>
        <div>
          <span class="text-purple-700 font-medium">Passo 4 de 4</span>
        </div>
      </div>
    </nav>

    <!-- Conteúdo principal -->
    <main class="flex-grow flex items-center justify-center px-4 pt-20 pb-16">
      <div class="bg-white rounded-2xl shadow-xl w-full max-w-md p-8">
        <div class="text-center mb-6">
          <div
            class="w-16 h-16 rounded-full bg-purple-100 flex items-center justify-center mx-auto mb-4"
          >
            <font-awesome-icon icon="envelope" class="text-purple-700 text-2xl" />
          </div>
          <h2 class="text-2xl font-bold text-purple-900">Verificação por E-mail</h2>
          <p class="text-gray-600 mt-2">Insira seu e-mail para receber o código de confirmação</p>
        </div>

        <form @submit.prevent="handleValidation" class="space-y-5">
          <!-- Campo de E-mail -->
          <div>
            <label class="block text-gray-700 mb-1">Endereço de E-mail</label>
            <input
              v-model="email"
              type="email"
              placeholder="ex: nome@exemplo.com"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
            />
          </div>

          <button
            type="button"
            @click="sendCode"
            class="btn-primary w-full py-3 text-white rounded-lg font-semibold"
            :disabled="sendingCode"
          >
            {{ sendingCode ? 'Enviando...' : 'Enviar Código' }}
          </button>

          <!-- Campo do Código -->
          <div v-if="codeSent" class="pt-4">
            <label class="block text-gray-700 mb-1">Código de Verificação</label>
            <input
              v-model="code"
              type="text"
              placeholder="Digite o código recebido"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
            />
          </div>

          <button
            v-if="codeSent"
            type="submit"
            class="w-full mt-4 py-3 bg-purple-700 text-white font-bold rounded-lg hover:bg-purple-800 transition"
            :disabled="validating"
          >
            {{ validating ? 'Validando...' : 'Validar e Finalizar Cadastro' }}
          </button>
        </form>
      </div>
    </main>

    <!-- Botão de voltar fora do card -->
    <div class="fixed bottom-4 left-4">
      <button
        @click="voltarParaCapturaFacial"
        class="bg-gray-300 text-gray-700 px-4 py-2 rounded-full font-medium hover:bg-gray-400 transition flex items-center"
      >
        <font-awesome-icon icon="arrow-left" class="mr-2" /> Voltar
      </button>
    </div>

    <!-- Pop-up de sucesso -->
    <div
      v-if="showSuccessModal"
      class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50"
    >
      <div class="bg-white rounded-2xl p-8 max-w-sm w-full mx-4 text-center">
        <div
          class="w-16 h-16 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-4"
        >
          <font-awesome-icon icon="check" class="text-green-600 text-2xl" />
        </div>
        <h3 class="text-2xl font-bold text-gray-800 mb-2">Cadastro Concluído!</h3>
        <p class="text-gray-600 mb-6">
          Seu cadastro foi concluído com sucesso. Agora você pode acessar todos os serviços Africel.
        </p>
        <button
          @click="redirectToHome"
          class="btn-primary w-full py-3 text-white rounded-lg font-semibold"
        >
          Ir para a página inicial
        </button>
      </div>
    </div>

    <!-- Pop-up de erro -->
    <div
      v-if="showErrorModal"
      class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50"
    >
      <div class="bg-white rounded-2xl p-8 max-w-sm w-full mx-4 text-center">
        <div
          class="w-16 h-16 rounded-full bg-red-100 flex items-center justify-center mx-auto mb-4"
        >
          <font-awesome-icon icon="exclamation-triangle" class="text-red-600 text-2xl" />
        </div>
        <h3 class="text-2xl font-bold text-gray-800 mb-2">Erro na Validação</h3>
        <p class="text-gray-600 mb-6">
          {{ errorMessage }}
        </p>
        <div class="flex space-x-4">
          <button
            @click="showErrorModal = false"
            class="flex-1 bg-gray-300 text-gray-700 py-3 rounded-lg font-medium"
          >
            Tentar Novamente
          </button>
          <button
            @click="voltarParaCapturaFacial"
            class="flex-1 bg-purple-700 text-white py-3 rounded-lg font-semibold"
          >
            Voltar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VerifyEmail',
  data() {
    return {
      email: '',
      code: '',
      codeSent: false,
      sendingCode: false,
      validating: false,
      showSuccessModal: false,
      showErrorModal: false,
      errorMessage: 'O código inserido é inválido ou expirou. Por favor, tente novamente.',
    }
  },
  methods: {
    async sendCode() {
      if (!this.validateEmail(this.email)) {
        this.showError('Por favor, insira um e-mail válido.')
        return
      }

      this.sendingCode = true

      try {
        // Simulação de envio de código por e-mail
        await new Promise((resolve) => setTimeout(resolve, 1500))
        this.codeSent = true
        this.showSuccess('Código enviado com sucesso! Verifique seu e-mail.')
      } catch (error) {
        this.showError('Falha ao enviar o código. Por favor, tente novamente.')
      } finally {
        this.sendingCode = false
      }
    },

    async handleValidation() {
      if (!this.code) {
        this.showError('Por favor, insira o código recebido.')
        return
      }

      this.validating = true

      try {
        // Simulação de validação do código
        await new Promise((resolve) => setTimeout(resolve, 1500))

        // Simulação: código válido é "123456"
        if (this.code === '123456') {
          // Simulação de registro completo
          await this.completeRegistration()
          this.showSuccessModal = true
        } else {
          throw new Error('Código inválido')
        }
      } catch (error) {
        this.showError('O código inserido é inválido ou expirou. Por favor, tente novamente.')
      } finally {
        this.validating = false
      }
    },

    async completeRegistration() {
      // Simulação de chamada API para finalizar cadastro
      return new Promise((resolve) => setTimeout(resolve, 1000))
    },

    validateEmail(email) {
      const re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return re.test(email)
    },

    showError(message) {
      this.errorMessage = message || 'Ocorreu um erro. Por favor, tente novamente.'
      this.showErrorModal = true
    },

    showSuccess(message) {
      // Em um caso real, poderia ser um toast notification
      console.log(message)
    },

    voltarParaCapturaFacial() {
      this.$router.push('/capture-photo')
    },

    redirectToHome() {
      this.showSuccessModal = false
      this.$router.push('/')
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
