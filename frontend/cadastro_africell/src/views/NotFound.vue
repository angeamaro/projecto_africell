<template>
  <div id="app">
    <!-- Navbar -->
    <nav class="fixed w-full z-50 bg-white shadow-md">
      <div class="container mx-auto px-4 py-3">
        <div class="flex justify-between items-center">
          <div class="flex items-center">
            <div class="flex items-center">
              <div class="w-10 h-10 rounded-full bg-purple-700 flex items-center justify-center">
                <div class="w-6 h-6 rounded-full bg-orange-500"></div>
              </div>
              <span class="ml-3 text-xl font-bold text-purple-900">AFRICEL</span>
            </div>
          </div>

          <!-- Desktop Navigation -->
          <div class="hidden md:flex items-center space-x-10">
            <a href="#home" class="text-gray-700 hover:text-purple-800 font-medium">Início</a>
            <a href="#problem" class="text-gray-700 hover:text-purple-800 font-medium"
              >Problemática</a
            >
            <a href="#solution" class="text-gray-700 hover:text-purple-800 font-medium">Solução</a>
            <a href="#impact" class="text-gray-700 hover:text-purple-800 font-medium">Impacto</a>
          </div>

          <div class="flex items-center">
            <button
              @click="showModal = true"
              class="hidden md:block bg-gradient-to-r from-orange-500 to-purple-700 text-white px-6 py-2 rounded-full font-semibold hover:shadow-lg transition-all duration-300"
            >
              Cadastrar-se
            </button>

            <!-- Mobile menu button -->
            <button @click="toggleMenu" class="md:hidden text-gray-700 focus:outline-none">
              <i class="fas fa-bars text-2xl"></i>
            </button>
          </div>
        </div>

        <!-- Mobile Menu -->
        <div v-show="isMenuOpen" class="md:hidden mt-4 pb-4">
          <div class="flex flex-col space-y-3">
            <a href="#home" class="text-gray-700 hover:text-purple-800 font-medium py-2">Início</a>
            <a href="#problem" class="text-gray-700 hover:text-purple-800 font-medium py-2"
              >Problemática</a
            >
            <a href="#solution" class="text-gray-700 hover:text-purple-800 font-medium py-2"
              >Solução</a
            >
            <a href="#impact" class="text-gray-700 hover:text-purple-800 font-medium py-2"
              >Impacto</a
            >
            <button
              @click="
                showModal = true,
                isMenuOpen = false
              "
              class="bg-gradient-to-r from-orange-500 to-purple-700 text-white px-6 py-2 rounded-full font-semibold mt-2"
            >
              Cadastrar-se
            </button>
          </div>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero-bg pt-32 pb-20 text-white">
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
                @click="showModal = true"
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
            <div class="relative">
              <div
                class="w-64 h-64 md:w-80 md:h-80 bg-white bg-opacity-20 rounded-full flex items-center justify-center animate-bounce-slow"
              >
                <div
                  class="w-56 h-56 md:w-72 md:h-72 bg-white bg-opacity-30 rounded-full flex items-center justify-center"
                >
                  <div
                    class="w-48 h-48 md:w-64 md:h-64 bg-white bg-opacity-40 rounded-full flex items-center justify-center"
                  >
                    <div class="bg-white p-6 rounded-2xl shadow-xl">
                      <div class="flex justify-center mb-4">
                        <div
                          class="w-16 h-16 rounded-full bg-purple-600 flex items-center justify-center"
                        >
                          <i class="fas fa-shield-alt text-white text-2xl"></i>
                        </div>
                      </div>
                      <h3 class="text-purple-900 font-bold text-center">Segurança</h3>
                      <p class="text-gray-700 text-sm text-center mt-2">Biometria Facial</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Wave Divider -->
    <div class="wave-divider"></div>

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

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div class="feature-card bg-white p-8 rounded-xl shadow-md">
            <div class="w-14 h-14 rounded-full bg-purple-100 flex items-center justify-center mb-6">
              <i class="fas fa-user-secret text-purple-700 text-2xl"></i>
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-3">Anonimato Criminoso</h3>
            <p class="text-gray-600">
              Criminosos utilizam números não rastreáveis para atividades ilícitas, dificultando
              investigações.
            </p>
          </div>

          <div class="feature-card bg-white p-8 rounded-xl shadow-md">
            <div class="w-14 h-14 rounded-full bg-orange-100 flex items-center justify-center mb-6">
              <i class="fas fa-shield-alt text-orange-500 text-2xl"></i>
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-3">Falhas de Segurança</h3>
            <p class="text-gray-600">
              Ausência de verificação de identidade compromete a segurança nacional e dos cidadãos.
            </p>
          </div>

          <div class="feature-card bg-white p-8 rounded-xl shadow-md">
            <div class="w-14 h-14 rounded-full bg-purple-100 flex items-center justify-center mb-6">
              <i class="fas fa-balance-scale text-purple-700 text-2xl"></i>
            </div>
            <h3 class="text-xl font-bold text-gray-800 mb-3">Dificuldade de Regulação</h3>
            <p class="text-gray-600">
              Órgãos reguladores enfrentam desafios para monitorar e controlar atividades ilícitas.
            </p>
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
            Sistema de cadastro biométrico completo para garantir segurança e conformidade
          </p>
        </div>

        <div class="flex flex-wrap items-center mb-16">
          <div class="w-full md:w-1/2 mb-10 md:mb-0">
            <div class="bg-white rounded-2xl overflow-hidden shadow-xl">
              <div class="p-1 bg-gradient-to-r from-orange-500 to-purple-700">
                <div class="bg-white p-6">
                  <div class="tabs flex border-b mb-6">
                    <button
                      @click="changeTab('problema')"
                      :class="{ 'tab-button active': activeTab === 'problema' }"
                      class="px-4 py-2 font-medium"
                    >
                      Problemática
                    </button>
                    <button
                      @click="changeTab('solucao')"
                      :class="{ 'tab-button active': activeTab === 'solucao' }"
                      class="px-4 py-2 font-medium"
                    >
                      Solução Africel
                    </button>
                  </div>

                  <div v-show="activeTab === 'problema'">
                    <h3 class="text-xl font-bold text-gray-800 mb-4">Sistema Atual Vulnerável</h3>
                    <ul class="space-y-3">
                      <li class="flex items-start">
                        <i class="fas fa-times-circle text-red-500 mt-1 mr-3"></i>
                        <span>Cadastro manual sem verificação</span>
                      </li>
                      <li class="flex items-start">
                        <i class="fas fa-times-circle text-red-500 mt-1 mr-3"></i>
                        <span>Dados inconsistentes e incompletos</span>
                      </li>
                      <li class="flex items-start">
                        <i class="fas fa-times-circle text-red-500 mt-1 mr-3"></i>
                        <span>Impossibilidade de rastreamento</span>
                      </li>
                      <li class="flex items-start">
                        <i class="fas fa-times-circle text-red-500 mt-1 mr-3"></i>
                        <span>Exposição a fraudes e crimes digitais</span>
                      </li>
                    </ul>
                  </div>

                  <div v-show="activeTab === 'solucao'">
                    <h3 class="text-xl font-bold text-gray-800 mb-4">Sistema de Cadastro Seguro</h3>
                    <ul class="space-y-3">
                      <li class="flex items-start">
                        <i class="fas fa-check-circle text-green-500 mt-1 mr-3"></i>
                        <span>Reconhecimento facial em tempo real</span>
                      </li>
                      <li class="flex items-start">
                        <i class="fas fa-check-circle text-green-500 mt-1 mr-3"></i>
                        <span>Validação automática com documento de identidade</span>
                      </li>
                      <li class="flex items-start">
                        <i class="fas fa-check-circle text-green-500 mt-1 mr-3"></i>
                        <span>Confirmação por SMS para ativação</span>
                      </li>
                      <li class="flex items-start">
                        <i class="fas fa-check-circle text-green-500 mt-1 mr-3"></i>
                        <span>Registro seguro e auditável</span>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="w-full md:w-1/2 px-0 md:px-10">
            <div class="grid grid-cols-2 gap-6">
              <div
                v-for="(step, index) in steps"
                :key="index"
                class="bg-white rounded-xl shadow-md p-6"
              >
                <div
                  class="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center mb-4"
                >
                  <i class="fas fa-{{step.icon}} text-purple-700"></i>
                </div>
                <h3 class="font-bold text-lg mb-2">{{ step.title }}</h3>
                <p class="text-gray-600 text-sm">{{ step.description }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Stats Section -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mt-16">
          <div
            v-for="(stat, index) in stats"
            :key="index"
            class="stat-card bg-white p-6 rounded-xl shadow-md text-center"
          >
            <div class="text-3xl font-bold text-purple-800 mb-2">{{ stat.value }}</div>
            <div class="text-gray-600">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Impact Section -->
    <section id="impact" class="py-20 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-purple-900 mb-4">Impacto Social</h2>
          <div class="h-1 w-20 bg-orange-500 mx-auto mb-6"></div>
          <p class="text-gray-700 max-w-3xl mx-auto text-lg">
            Como nosso sistema transformará a segurança digital em Angola
          </p>
        </div>

        <div class="flex flex-col md:flex-row items-center">
          <div class="md:w-1/2 mb-10 md:mb-0">
            <div class="bg-white rounded-2xl shadow-xl p-8">
              <h3 class="text-2xl font-bold text-gray-800 mb-6">Benefícios do Sistema</h3>

              <div class="space-y-6">
                <div class="flex">
                  <div class="flex-shrink-0">
                    <div
                      class="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center"
                    >
                      <i class="fas fa-lock text-green-600"></i>
                    </div>
                  </div>
                  <div class="ml-4">
                    <h4 class="text-lg font-semibold text-gray-800">
                      Segurança Nacional Fortalecida
                    </h4>
                    <p class="text-gray-600 mt-1">
                      Redução significativa de atividades criminosas realizadas através de números
                      anônimos.
                    </p>
                  </div>
                </div>

                <div class="flex">
                  <div class="flex-shrink-0">
                    <div
                      class="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center"
                    >
                      <i class="fas fa-user-shield text-blue-600"></i>
                    </div>
                  </div>
                  <div class="ml-4">
                    <h4 class="text-lg font-semibold text-gray-800">Proteção ao Cidadão</h4>
                    <p class="text-gray-600 mt-1">
                      Dados pessoais protegidos e uso responsável de informações.
                    </p>
                  </div>
                </div>

                <div class="flex">
                  <div class="flex-shrink-0">
                    <div
                      class="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center"
                    >
                      <i class="fas fa-balance-scale text-purple-600"></i>
                    </div>
                  </div>
                  <div class="ml-4">
                    <h4 class="text-lg font-semibold text-gray-800">Conformidade Regulatória</h4>
                    <p class="text-gray-600 mt-1">
                      Sistema totalmente alinhado com as regulamentações nacionais de
                      telecomunicações.
                    </p>
                  </div>
                </div>

                <div class="flex">
                  <div class="flex-shrink-0">
                    <div
                      class="w-12 h-12 rounded-full bg-orange-100 flex items-center justify-center"
                    >
                      <i class="fas fa-chart-line text-orange-500"></i>
                    </div>
                  </div>
                  <div class="ml-4">
                    <h4 class="text-lg font-semibold text-gray-800">Transparência Operacional</h4>
                    <p class="text-gray-600 mt-1">
                      Processos auditáveis e rastreáveis para todas as operações.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="md:w-1/2 md:pl-12">
            <div class="bg-gradient-to-br from-purple-700 to-orange-500 rounded-2xl p-8 text-white">
              <h3 class="text-2xl font-bold mb-6">Impacto Esperado</h3>

              <div class="space-y-4">
                <div class="flex items-center">
                  <div
                    class="w-8 h-8 rounded-full bg-white bg-opacity-20 flex items-center justify-center mr-4"
                  >
                    <i class="fas fa-check"></i>
                  </div>
                  <span>Redução de 80% em crimes digitais em 2 anos</span>
                </div>

                <div class="flex items-center">
                  <div
                    class="w-8 h-8 rounded-full bg-white bg-opacity-20 flex items-center justify-center mr-4"
                  >
                    <i class="fas fa-check"></i>
                  </div>
                  <span>Cadastro de 100% dos novos usuários com biometria</span>
                </div>

                <div class="flex items-center">
                  <div
                    class="w-8 h-8 rounded-full bg-white bg-opacity-20 flex items-center justify-center mr-4"
                  >
                    <i class="fas fa-check"></i>
                  </div>
                  <span>Integração com sistemas de segurança nacional</span>
                </div>

                <div class="flex items-center">
                  <div
                    class="w-8 h-8 rounded-full bg-white bg-opacity-20 flex items-center justify-center mr-4"
                  >
                    <i class="fas fa-check"></i>
                  </div>
                  <span>Referência em segurança digital na África</span>
                </div>
              </div>

              <div class="mt-8 pt-6 border-t border-white border-opacity-20">
                <p class="text-lg font-semibold">
                  "A Africel está comprometida em liderar a transformação digital segura em Angola"
                </p>
                <p class="mt-2 opacity-80">- Diretoria de Segurança Digital</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-r from-purple-800 to-orange-600 text-white">
      <div class="container mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-6">Proteja sua identidade digital</h2>
        <p class="text-xl max-w-2xl mx-auto mb-10 opacity-90">
          Faça parte da nova era de segurança digital em Angola. Cadastre-se agora e tenha seu
          número protegido.
        </p>
        <button
          @click="showModal = true"
          class="bg-white text-purple-800 px-8 py-4 rounded-full font-bold text-lg shadow-lg hover:bg-gray-100 transition duration-300"
        >
          Cadastrar-se Agora
        </button>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white pt-16 pb-8">
      <div class="container mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between">
          <div class="mb-10 md:mb-0">
            <div class="flex items-center mb-6">
              <div class="w-10 h-10 rounded-full bg-purple-700 flex items-center justify-center">
                <div class="w-6 h-6 rounded-full bg-orange-500"></div>
              </div>
              <span class="ml-3 text-xl font-bold">AFRICEL</span>
            </div>
            <p class="max-w-xs text-gray-400">
              Liderando a revolução digital segura em Angola com tecnologia inovadora e compromisso
              social.
            </p>
          </div>

          <div class="grid grid-cols-2 md:grid-cols-3 gap-8">
            <div>
              <h4 class="text-lg font-bold mb-4">Links Rápidos</h4>
              <ul class="space-y-2">
                <li><a href="#home" class="text-gray-400 hover:text-white">Início</a></li>
                <li><a href="#problem" class="text-gray-400 hover:text-white">Problemática</a></li>
                <li><a href="#solution" class="text-gray-400 hover:text-white">Solução</a></li>
                <li><a href="#impact" class="text-gray-400 hover:text-white">Impacto</a></li>
              </ul>
            </div>

            <div>
              <h4 class="text-lg font-bold mb-4">Recursos</h4>
              <ul class="space-y-2">
                <li><a href="#" class="text-gray-400 hover:text-white">Perguntas Frequentes</a></li>
                <li><a href="#" class="text-gray-400 hover:text-white">Documentação</a></li>
                <li>
                  <a href="#" class="text-gray-400 hover:text-white">Política de Privacidade</a>
                </li>
                <li><a href="#" class="text-gray-400 hover:text-white">Termos de Uso</a></li>
              </ul>
            </div>

            <div>
              <h4 class="text-lg font-bold mb-4">Contato</h4>
              <ul class="space-y-2 text-gray-400">
                <li class="flex items-start">
                  <i class="fas fa-map-marker-alt mt-1 mr-3"></i>
                  <span>Luanda, Angola</span>
                </li>
                <li class="flex items-start">
                  <i class="fas fa-phone mt-1 mr-3"></i>
                  <span>+244 923 456 789</span>
                </li>
                <li class="flex items-start">
                  <i class="fas fa-envelope mt-1 mr-3"></i>
                  <span>suporte@africel.ao</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="border-t border-gray-800 mt-12 pt-8 text-center text-gray-500">
          <p>&copy; 2023 Africel Telecomunicações. Todos os direitos reservados.</p>
        </div>
      </div>
    </footer>

    <!-- Registration Modal -->
    <div v-show="showModal" class="fixed inset-0 z-50 overflow-y-auto">
      <div class="modal-overlay fixed inset-0 bg-black bg-opacity-70"></div>

      <div class="flex items-center justify-center min-h-screen">
        <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md mx-4 relative">
          <button
            @click="showModal = false"
            class="absolute top-4 right-4 text-gray-500 hover:text-gray-700"
          >
            <i class="fas fa-times text-xl"></i>
          </button>

          <div v-if="!registrationSuccess" class="p-8">
            <div class="text-center mb-6">
              <div
                class="w-16 h-16 rounded-full bg-purple-100 flex items-center justify-center mx-auto mb-4"
              >
                <i class="fas fa-user-plus text-purple-700 text-2xl"></i>
              </div>
              <h3 class="text-2xl font-bold text-gray-800 mb-2">Cadastre-se Agora</h3>
              <p class="text-gray-600">Preencha os dados para iniciar seu cadastro biométrico</p>
            </div>

            <form @submit.prevent="submitForm">
              <div class="space-y-4">
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
                  <label class="block text-gray-700 mb-2">Email</label>
                  <input
                    v-model="formData.email"
                    type="email"
                    required
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
                  />
                </div>

                <div>
                  <label class="block text-gray-700 mb-2">Número do Bilhete de Identidade</label>
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
              </div>
            </form>
          </div>

          <div v-else class="p-8 text-center">
            <div
              class="w-20 h-20 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-6"
            >
              <i class="fas fa-check-circle text-green-500 text-4xl"></i>
            </div>
            <h3 class="text-2xl font-bold text-gray-800 mb-2">Cadastro Iniciado!</h3>
            <p class="text-gray-600 mb-6">
              Você receberá um SMS com instruções para completar seu cadastro biométrico.
            </p>
            <button
              @click="showModal = false"
              class="bg-purple-700 text-white px-6 py-2 rounded-lg font-medium"
            >
              Fechar
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
window.onload = function () {
  new Vue({
    el: '#app',
    data: {
      isMenuOpen: false,
      formData: {
        name: '',
        phone: '',
        email: '',
        bi: '',
      },
      showModal: false,
      registrationSuccess: false,
      activeTab: 'problema',
      steps: [
        {
          title: 'Reconhecimento Facial',
          description: 'Captura em tempo real com múltiplos ângulos para máxima segurança',
          icon: 'face',
        },
        {
          title: 'Comparação com BI',
          description: 'Validação automática com documento de identidade oficial',
          icon: 'badge',
        },
        {
          title: 'Ativação por SMS',
          description: 'Confirmação final através de código enviado para seu número',
          icon: 'sms',
        },
        {
          title: 'Registro Seguro',
          description: 'Armazenamento auditável e criptografado dos dados',
          icon: 'lock',
        },
      ],
      stats: [
        { value: '95%', label: 'Redução de fraudes' },
        { value: '99%', label: 'Precisão biométrica' },
        { value: '24/7', label: 'Disponibilidade' },
        { value: '100%', label: 'Conformidade legal' },
      ],
    },
    methods: {
      toggleMenu() {
        this.isMenuOpen = !this.isMenuOpen
      },
      submitForm() {
        // Simulando cadastro bem-sucedido
        this.registrationSuccess = true
        this.showModal = true

        // Reset form
        this.formData = { name: '', phone: '', email: '', bi: '' }

        // Fechar modal após 3 segundos
        setTimeout(() => {
          this.showModal = false
        }, 3000)
      },
      changeTab(tab) {
        this.activeTab = tab
      },
    },
  })
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

body {
  font-family: 'Inter', sans-serif;
  background: linear-gradient(135deg, #f4f4f4 0%, #ffffff 100%);
  scroll-behavior: smooth;
}

.hero-bg {
  background:
    linear-gradient(135deg, rgba(102, 45, 145, 0.9) 0%, rgba(243, 112, 33, 0.85) 100%),
    url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><rect width="100" height="100" fill="%23662D91" opacity="0.1"/><path d="M0 50 L100 50 M50 0 L50 100" stroke="%23F37021" stroke-width="1" opacity="0.1"/></svg>');
  background-size: cover;
  background-position: center;
}

.card-gradient {
  background: linear-gradient(145deg, #ffffff 0%, #f4f4f4 100%);
  box-shadow: 0 10px 25px rgba(102, 45, 145, 0.1);
  border-radius: 16px;
}

.feature-card {
  transition: all 0.3s ease;
  border-left: 4px solid #f37021;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(102, 45, 145, 0.15);
}

.tab-button {
  transition: all 0.3s ease;
  border-bottom: 3px solid transparent;
}

.tab-button.active {
  border-bottom: 3px solid #f37021;
  color: #662d91;
  font-weight: 600;
}

.btn-primary {
  background: linear-gradient(90deg, #f37021 0%, #662d91 100%);
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(102, 45, 145, 0.25);
}

.btn-secondary {
  background: #662d91;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: #4a1f6e;
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(102, 45, 145, 0.25);
}

.stat-card {
  transition: all 0.3s ease;
  border-top: 4px solid #f37021;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(102, 45, 145, 0.15);
}

.modal-overlay {
  background: rgba(0, 0, 0, 0.7);
}

.animate-bounce-slow {
  animation: bounce-slow 2s infinite;
}

@keyframes bounce-slow {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-15px);
  }
}

.wave-divider {
  height: 50px;
  background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="%23F4F4F4" fill-opacity="1" d="M0,160L48,149.3C96,139,192,117,288,112C384,107,480,117,576,128C672,139,768,149,864,138.7C960,128,1056,96,1152,96C1248,96,1344,128,1392,144L1440,160L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>');
  background-size: cover;
  background-position: center;
}
</style>
