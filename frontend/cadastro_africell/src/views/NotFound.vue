<template>
  <div class="not-found">
    <!-- Navbar (mantendo o mesmo estilo) -->
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
            <router-link
              to="/"
              class="hidden md:block bg-gradient-to-r from-orange-500 to-purple-700 text-white px-6 py-2 rounded-full font-semibold hover:shadow-lg transition-all duration-300"
            >
              Voltar ao Início
            </router-link>
          </div>
        </div>

        <!-- Mobile Menu -->
        <div class="md:hidden mt-4 pb-4">
          <router-link
            to="/"
            class="w-full bg-gradient-to-r from-orange-500 to-purple-700 text-white px-6 py-2 rounded-full font-semibold text-center block"
          >
            Voltar ao Início
          </router-link>
        </div>
      </div>
    </nav>

    <!-- Conteúdo principal da página 404 -->
    <main class="min-h-screen pt-32 pb-20">
      <div class="container mx-auto px-4">
        <div class="max-w-3xl mx-auto text-center">
          <!-- Ícone de erro -->
          <div
            class="mx-auto mb-8 w-32 h-32 rounded-full bg-red-100 flex items-center justify-center"
          >
            <div class="text-red-600 text-6xl">!</div>
          </div>

          <h1 class="text-6xl md:text-8xl font-bold text-purple-900 mb-4">404</h1>

          <h2 class="text-2xl md:text-3xl font-bold text-gray-800 mb-6">Página não encontrada</h2>

          <p class="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">
            Desculpe, a página que você está procurando não existe ou foi movida.
          </p>

          <div class="flex flex-col sm:flex-row justify-center gap-4">
            <router-link
              to="/"
              class="btn-primary text-white px-8 py-3 rounded-full font-bold text-lg inline-block"
            >
              Página Inicial
            </router-link>

            <a
              href="#"
              @click.prevent="$router.go(-1)"
              class="bg-gray-200 text-gray-800 px-8 py-3 rounded-full font-bold text-lg inline-block hover:bg-gray-300 transition"
            >
              Voltar
            </a>
          </div>
        </div>

        <!-- Ilustração -->
        <div class="mt-16 max-w-lg mx-auto">
          <div class="relative">
            <div
              class="absolute -inset-4 bg-gradient-to-r from-orange-500 to-purple-700 rounded-2xl rotate-6"
            ></div>
            <div class="relative bg-white rounded-2xl p-8 text-center shadow-lg">
              <font-awesome-icon
                icon="exclamation-triangle"
                class="text-6xl text-yellow-500 mb-4"
              />
              <p class="text-gray-700">
                Você tentou acessar: <br />
                <span class="font-mono text-sm break-all">{{ $route.path }}</span>
              </p>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Footer (mantendo o mesmo estilo) -->
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
  </div>
</template>

<script>
export default {
  name: 'NotFoundView',
}
</script>

<style scoped>
.not-found {
  background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%);
}

.btn-primary {
  background: linear-gradient(90deg, #f37021 0%, #662d91 100%);
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(102, 45, 145, 0.25);
}

/* Mantendo os estilos de responsividade */
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
</style>
