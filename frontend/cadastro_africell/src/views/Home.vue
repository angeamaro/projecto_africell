<template>
  <div class="home">
    <!-- Navbar -->
    <nav class="fixed w-full z- bg-white shadow-md">
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
            <button
              @click="irParaUploadBI"
              class="hidden md:block bg-gradient-to-r from-orange-500 to-purple-700 text-white px-6 py-2 rounded-full font-semibold hover:shadow-lg transition-all duration-300"
            >
              Cadastrar-se
            </button>
          </div>
        </div>

        <!-- Mobile Menu -->
        <div v-show="isMenuOpen" class="md:hidden mt-4 pb-4">
          <button
            @click="irParaUploadBI"
            class="w-full bg-gradient-to-r from-orange-500 to-purple-700 text-white px-6 py-2 rounded-full font-semibold"
          >
            Cadastrar-se
          </button>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-bg pt-32 pb-20 text-white">
      <div class="container mx-auto px-4">
        <div class="flex flex-col md:flex-row items-center">
          <div class="md:w-1/2 mb-10 md:mb-0">
            <h1 class="text-4xl md:text-5xl font-bold leading-tight mb-4">
              Cadastro Seguro de Números Telefônicos
            </h1>
            <p class="text-xl mb-8 opacity-90">
              A solução inovadora da Africel para garantir segurança nacional e combater o anonimato
              em crimes digitais.
            </p>
            <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
              <button
                @click="irParaUploadBI"
                class="btn-primary text-white px-8 py-3 rounded-full font-bold text-lg"
              >
                Cadastrar-se Agora
              </button>
              <a
                href="#solution"
                class="bg-white text-purple-800 px-8 py-3 rounded-full font-bold text-lg text-center"
              >
                Saiba Mais
              </a>
            </div>
          </div>
          <div class="md:w-1/2 flex justify-center">
            <div class="bg-white p-6 rounded-2xl shadow-xl text-center">
              <div class="flex justify-center mb-4">
                <div class="w-16 h-16 rounded-full bg-purple-600 flex items-center justify-center">
                  <font-awesome-icon icon="shield-alt" class="text-white text-2xl" />
                </div>
              </div>
              <h3 class="text-purple-900 font-bold">Segurança</h3>
              <p class="text-gray-700 text-sm mt-2">Biometria Facial</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Problem Section -->
    <section id="problem" class="py-16 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-purple-900 mb-4">A Problemática</h2>
          <div class="h-1 w-20 bg-orange-500 mx-auto mb-6"></div>
          <p class="text-gray-700 max-w-3xl mx-auto text-lg">
            A venda de cartões SIM sem cadastro estruturado compromete a segurança nacional e
            permite o anonimato para crimes digitais.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="feature-card bg-white p-8 rounded-xl shadow-md">
            <div class="w-14 h-14 rounded-full bg-purple-100 flex items-center justify-center mb-6">
              <font-awesome-icon icon="user-secret" class="text-purple-700 text-2xl" />
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-3">Anonimato Criminoso</h3>
            <p class="text-gray-600">
              Criminosos utilizam números não rastreáveis para atividades ilícitas.
            </p>
          </div>

          <div class="feature-card bg-white p-8 rounded-xl shadow-md">
            <div class="w-14 h-14 rounded-full bg-orange-100 flex items-center justify-center mb-6">
              <font-awesome-icon icon="shield-alt" class="text-orange-500 text-2xl" />
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-3">Falhas de Segurança</h3>
            <p class="text-gray-600">
              Ausência de verificação de identidade compromete a segurança.
            </p>
          </div>

          <div class="feature-card bg-white p-8 rounded-xl shadow-md">
            <div class="w-14 h-14 rounded-full bg-purple-100 flex items-center justify-center mb-6">
              <font-awesome-icon icon="balance-scale" class="text-purple-700 text-2xl" />
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-3">Dificuldade de Regulação</h3>
            <p class="text-gray-600">Desafios para monitorar e controlar atividades ilícitas.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Solution Section -->
    <section id="solution" class="py-20">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-purple-900 mb-4">Nossa Solução</h2>
          <div class="h-1 w-20 bg-orange-500 mx-auto mb-6"></div>
          <p class="text-gray-700 max-w-3xl mx-auto text-lg">
            Sistema de cadastro biométrico completo para garantir segurança
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="bg-white rounded-xl shadow-md p-6 text-center">
            <div
              class="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center mb-4 mx-auto"
            >
              <font-awesome-icon icon="face-smile" class="text-purple-700" />
            </div>
            <h3 class="font-bold text-lg mb-2">Reconhecimento Facial</h3>
            <p class="text-gray-600 text-sm">Captura em tempo real com múltiplos ângulos</p>
          </div>

          <div class="bg-white rounded-xl shadow-md p-6 text-center">
            <div
              class="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center mb-4 mx-auto"
            >
              <font-awesome-icon icon="id-card" class="text-purple-700" />
            </div>
            <h3 class="font-bold text-lg mb-2">Comparação com BI</h3>
            <p class="text-gray-600 text-sm">Validação com documento de identidade</p>
          </div>

          <div class="bg-white rounded-xl shadow-md p-6 text-center">
            <div
              class="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center mb-4 mx-auto"
            >
              <font-awesome-icon icon="sms" class="text-purple-700" />
            </div>
            <h3 class="font-bold text-lg mb-2">Ativação por SMS</h3>
            <p class="text-gray-600 text-sm">Confirmação final via código</p>
          </div>

          <div class="bg-white rounded-xl shadow-md p-6 text-center">
            <div
              class="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center mb-4 mx-auto"
            >
              <font-awesome-icon icon="lock" class="text-purple-700" />
            </div>
            <h3 class="font-bold text-lg mb-2">Registro Seguro</h3>
            <p class="text-gray-600 text-sm">Armazenamento auditável e criptografado</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-r from-purple-800 to-orange-600 text-white">
      <div class="container mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-6">Proteja sua identidade digital</h2>
        <p class="text-xl max-w-2xl mx-auto mb-10 opacity-90">
          Faça parte da nova era de segurança digital em Angola
        </p>
        <button
          @click="irParaUploadBI"
          class="bg-white text-purple-800 px-8 py-4 rounded-full font-bold text-lg shadow-lg hover:bg-gray-100 transition duration-300"
        >
          Cadastrar-se Agora
        </button>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white pt-16 pb-8">
      <div class="container mx-auto px-4 text-center">
        <div class="flex items-center justify-center mb-6">
          <div class="w-10 h-10 rounded-full bg-purple-700 flex items-center justify-center">
            <div class="w-6 h-6 rounded-full bg-orange-500"></div>
          </div>
          <span class="ml-3 text-xl font-bold">AFRICEL</span>
        </div>
        <p class="max-w-md mx-auto text-gray-400 mb-8">
          Liderando a revolução digital segura em Angola
        </p>

        <div class="border-t border-gray-800 mt-8 pt-8 text-center text-gray-500">
          <p>&copy; 2023 Africel Telecomunicações. Todos os direitos reservados.</p>
        </div>
      </div>
    </footer>

    <!-- Registration Modal -->
    <div
      v-if="showModal"
      class="fixed inset-0 z-50 overflow-y-auto bg-black bg-opacity-70 flex items-center justify-center"
    >
      <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md mx-4 relative p-8">
        <button class="absolute top-4 right-4 text-gray-500 hover:text-gray-700">
          <font-awesome-icon icon="times" class="text-xl" />
        </button>

        <div class="text-center mb-6">
          <div
            class="w-16 h-16 rounded-full bg-purple-100 flex items-center justify-center mx-auto mb-4"
          >
            <font-awesome-icon icon="user-plus" class="text-purple-700 text-2xl" />
          </div>
          <h3 class="text-2xl font-bold text-gray-800 mb-2">Cadastre-se Agora</h3>
          <p class="text-gray-600">Preencha os dados para iniciar seu cadastro biométrico</p>
        </div>

        <form @submit.prevent="submitForm" class="space-y-4">
          <div>
            <label class="block text-gray-700 mb-2">Nome Completo</label>
            <input
              v-model="formData.name"
              type="text"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
            />
          </div>

          <div>
            <label class="block text-gray-700 mb-2">Número de Telefone</label>
            <input
              v-model="formData.phone"
              type="tel"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
            />
          </div>

          <div>
            <label class="block text-gray-700 mb-2">Número do BI</label>
            <input
              v-model="formData.bi"
              type="text"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
            />
          </div>

          <div class="pt-4">
            <button
              type="submit"
              class="btn-primary w-full text-white py-3 rounded-lg font-semibold"
            >
              Iniciar Cadastro Biométrico
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      isMenuOpen: false,
      showModal: false,
      registrationSuccess: false,
      formData: {
        name: '',
        phone: '',
        bi: '',
      },
    }
  },
  methods: {
    irParaUploadBI() {
      this.$router.push('/upload-bi')
    },
    submitForm() {
      // Simulação de cadastro
      this.registrationSuccess = true

      // Fechar modal após 2 segundos
      setTimeout(() => {
        this.showModal = false
        this.registrationSuccess = false
      }, 2000)
    },
  },
}
</script>

<style scoped>
/* Fontes e cores base */
body {
  font-family: 'Inter', sans-serif;
  width: 100%;
  background: linear-gradient(135deg, #f4f4f4 0%, #ffffff 100%);
  scroll-behavior: smooth;
}

/* Hero section */
.hero-bg {
  background: linear-gradient(135deg, rgba(102, 45, 145, 0.9) 0%, rgba(243, 112, 33, 0.85) 100%);
}

/* Botões */
.btn-primary {
  background: linear-gradient(90deg, #f37021 0%, #662d91 100%);
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(102, 45, 145, 0.25);
}

/* Cards de features */
.feature-card {
  transition: all 0.3s ease;
  border-left: 4px solid #f37021;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(102, 45, 145, 0.15);
}

/* Responsividade */
.container {
  width: 100%;
  padding-right: 1rem;
  padding-left: 1rem;
  margin-right: auto;
  margin-left: auto;
}

@media (min-width: 640px) {
  .container {
    max-width: 640px;
  }
}

@media (min-width: 768px) {
  .container {
    max-width: 768px;
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
}

@media (min-width: 1280px) {
  .container {
    max-width: 1280px;
  }
}

/* Utilitários */
.text-purple-900 {
  color: #662d91;
}
.text-orange-500 {
  color: #f37021;
}
.bg-purple-700 {
  background-color: #662d91;
}
.bg-orange-500 {
  background-color: #f37021;
}
.bg-purple-100 {
  background-color: #e9d8fd;
}
.bg-orange-100 {
  background-color: #ffedd5;
}
.bg-gray-50 {
  background-color: #f4f4f4;
}
.bg-gray-900 {
  background-color: #1a202c;
}
.text-white {
  color: white;
}
.text-gray-700 {
  color: #4a5568;
}
.text-gray-600 {
  color: #718096;
}
.text-gray-400 {
  color: #cbd5e0;
}
.text-gray-800 {
  color: #2d3748;
}
.rounded-full {
  border-radius: 9999px;
}
.rounded-xl {
  border-radius: 0.75rem;
}
.rounded-2xl {
  border-radius: 1rem;
}
.shadow-md {
  box-shadow:
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
.shadow-lg {
  box-shadow:
    0 10px 15px -3px rgba(0, 0, 0, 0.1),
    0 4px 6px -2px rgba(0, 0, 0, 0.05);
}
.shadow-xl {
  box-shadow:
    0 20px 25px -5px rgba(0, 0, 0, 0.1),
    0 10px 10px -5px rgba(0, 0, 0, 0.04);
}
.z-50 {
  z-index: 50;
}
.fixed {
  position: fixed;
}
.w-full {
  width: 100%;
}
.flex {
  display: flex;
}
.justify-between {
  justify-content: space-between;
}
.items-center {
  align-items: center;
}
.hidden {
  display: none;
}
@media (min-width: 768px) {
  .md\:flex {
    display: flex;
  }
  .md\:hidden {
    display: none;
  }
  .md\:block {
    display: block;
  }
}
</style>
