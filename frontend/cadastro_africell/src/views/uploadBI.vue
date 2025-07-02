<template>
  <div class="upload-bi">
    <!-- Navbar -->
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
            <span class="text-purple-700 font-medium">Passo 1 de 4</span>
          </div>
        </div>
      </div>
    </nav>

    <!-- Conteúdo Principal -->
    <main class="pt-20 pb-10 container mx-auto px-4">
      <div class="max-w-3xl mx-auto">
        <!-- Título -->
        <h1 class="text-3xl md:text-4xl font-bold text-purple-900 text-center mb-8">
          Enviar Bilhete de Identidade
        </h1>

        <!-- Instruções -->
        <div class="bg-purple-50 rounded-xl p-6 mb-8">
          <h2 class="text-xl font-bold text-purple-800 mb-4">Instruções para fotografia do BI:</h2>
          <ul class="list-disc pl-5 space-y-2 text-gray-700">
            <li>Certifique-se de que o BI está dentro do prazo de validade</li>
            <li>Coloque o BI sobre uma superfície plana e escura</li>
            <li>Certifique-se de que toda a informação está legível</li>
            <li>Evite reflexos e sombras sobre o documento</li>
            <li>Use uma iluminação adequada (nem muito forte, nem fraca)</li>
          </ul>
        </div>

        <!-- Área de Upload -->
        <div class="bg-white rounded-xl shadow-md p-6 mb-8">
          <div v-if="!imagePreview">
            <label
              for="bi-upload"
              class="flex flex-col items-center justify-center border-2 border-dashed border-purple-300 rounded-xl h-64 cursor-pointer hover:bg-purple-50 transition"
            >
              <div class="text-purple-700 mb-4">
                <font-awesome-icon icon="cloud-upload-alt" class="text-4xl" />
              </div>
              <p class="text-lg font-medium text-purple-900">Clique para enviar a foto do seu BI</p>
              <p class="text-gray-500 mt-2">Formatos aceitos: JPG, PNG (Máx. 5MB)</p>
            </label>
            <input
              id="bi-upload"
              type="file"
              accept="image/*"
              class="hidden"
              @change="handleImageUpload"
            />
          </div>

          <!-- Preview da Imagem -->
          <div v-else class="text-center">
            <div class="relative mx-auto max-w-md">
              <img :src="imagePreview" alt="Preview BI" class="rounded-xl max-h-80 mx-auto" />
              <button
                @click="removeImage"
                class="absolute top-2 right-2 bg-red-500 text-white rounded-full p-2 hover:bg-red-600"
              >
                <font-awesome-icon icon="times" />
              </button>
            </div>
            <p class="text-gray-700 mt-4">Imagem selecionada: {{ fileName }}</p>
          </div>

          <!-- Mensagens de Erro -->
          <div v-if="error" class="mt-4 text-center text-red-500">
            {{ error }}
          </div>
        </div>

        <!-- Botão de Envio -->
        <div class="text-center">
          <button
            @click="submitBI"
            :disabled="!imagePreview || loading"
            class="btn-primary text-white px-8 py-4 rounded-full font-bold text-lg disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="loading">
              <font-awesome-icon icon="spinner" spin class="mr-2" /> Enviando...
            </span>
            <span v-else>Enviar BI</span>
          </button>
        </div>

        <!-- Feedback de Sucesso -->
        <div v-if="success" class="mt-8 bg-green-100 text-green-700 rounded-xl p-4 text-center">
          <font-awesome-icon icon="check-circle" class="mr-2" />
          BI enviado com sucesso! Estamos validando seus dados.
        </div>
      </div>
    </main>

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
  </div>
</template>

<script>
export default {
  name: 'UploadBI',
  data() {
    return {
      imagePreview: null,
      fileName: '',
      error: '',
      loading: false,
      success: false,
    }
  },
  methods: {
    handleImageUpload(event) {
      const file = event.target.files[0]
      if (!file) return

      // Validação do tipo de arquivo
      const validTypes = ['image/jpeg', 'image/png']
      if (!validTypes.includes(file.type)) {
        this.error = 'Formato inválido. Por favor, envie uma imagem JPG ou PNG.'
        return
      }

      // Validação do tamanho (5MB)
      const maxSize = 5 * 1024 * 1024 // 5MB
      if (file.size > maxSize) {
        this.error = 'Arquivo muito grande. O tamanho máximo é 5MB.'
        return
      }

      // Resetar erros
      this.error = ''

      // Preview da imagem
      const reader = new FileReader()
      reader.onload = (e) => {
        this.imagePreview = e.target.result
        this.fileName = file.name
      }
      reader.readAsDataURL(file)
    },
    removeImage() {
      this.imagePreview = null
      this.fileName = ''
    },
    submitBI() {
      if (!this.imagePreview) {
        this.error = 'Por favor, selecione uma imagem do BI.'
        return
      }

      this.loading = true
      this.error = ''

      // Simulação de envio (substituir por chamada API real)
      setTimeout(() => {
        this.loading = false
        this.success = true

        // Redirecionar após 2 segundos (simulação)
        setTimeout(() => {
          this.$router.push('/confirm-data')
        }, 2000)
      }, 1500)
    },
  },
}
</script>

<style scoped>
.upload-bi {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Reutilizando estilos da home */
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

/* Botão primário */
.btn-primary {
  background: linear-gradient(90deg, #f37021 0%, #662d91 100%);
  transition: all 0.3s ease;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(102, 45, 145, 0.25);
}

/* Utilitários de cor */
.text-purple-900 {
  color: #662d91;
}
.text-purple-800 {
  color: #5a2590;
}
.bg-purple-50 {
  background-color: #f5f3ff;
}
.bg-purple-700 {
  background-color: #662d91;
}
.bg-orange-500 {
  background-color: #f37021;
}
.bg-white {
  background-color: #fff;
}
.text-white {
  color: #fff;
}
.text-gray-700 {
  color: #4a5568;
}
.text-gray-500 {
  color: #718096;
}
.text-red-500 {
  color: #e53e3e;
}
.text-green-700 {
  color: #2f855a;
}
.bg-green-100 {
  background-color: #f0fff4;
}
.bg-red-500 {
  background-color: #e53e3e;
}
.bg-gray-900 {
  background-color: #1a202c;
}
.text-gray-400 {
  color: #cbd5e0;
}

/* Utilitários de forma */
.rounded-xl {
  border-radius: 0.75rem;
}
.rounded-full {
  border-radius: 9999px;
}

/* Utilitários de layout */
.flex {
  display: flex;
}
.flex-col {
  flex-direction: column;
}
.items-center {
  align-items: center;
}
.justify-center {
  justify-content: center;
}
.text-center {
  text-align: center;
}
.mb-8 {
  margin-bottom: 2rem;
}
.mt-4 {
  margin-top: 1rem;
}
.mt-8 {
  margin-top: 2rem;
}
.p-6 {
  padding: 1.5rem;
}
.pt-20 {
  padding-top: 5rem;
}
.pb-10 {
  padding-bottom: 2.5rem;
}
.relative {
  position: relative;
}
.absolute {
  position: absolute;
}
.hidden {
  display: none;
}
.w-full {
  width: 100%;
}
.max-w-3xl {
  max-width: 48rem;
}
.mx-auto {
  margin-left: auto;
  margin-right: auto;
}
.cursor-pointer {
  cursor: pointer;
}
.h-64 {
  height: 16rem;
}

/* Área de upload */
.border-dashed {
  border-style: dashed;
}
.border-2 {
  border-width: 2px;
}
.border-purple-300 {
  border-color: #d8b4fe;
}
.hover\:bg-purple-50:hover {
  background-color: #f5f3ff;
}
.transition {
  transition-property:
    background-color, border-color, color, fill, stroke, opacity, box-shadow, transform;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
</style>
