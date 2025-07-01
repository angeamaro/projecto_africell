<template>
  <div class="confirm-data">
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
            <span class="text-purple-700 font-medium">Passo 2 de 5</span>
          </div>
        </div>
      </div>
    </nav>

    <!-- Conteúdo Principal -->
    <main class="pt-20 pb-10 container mx-auto px-4">
      <div class="max-w-3xl mx-auto">
        <!-- Título -->
        <div class="text-center mb-8">
          <h1 class="text-3xl md:text-4xl font-bold text-purple-900 mb-4">Confirme seus dados</h1>
          <p class="text-gray-700 max-w-2xl mx-auto text-lg">
            Verifique as informações extraídas do seu BI e complete quando necessário
          </p>
          <div class="h-1 w-20 bg-orange-500 mx-auto my-6"></div>
        </div>

        <!-- Dados Extraídos do BI -->
        <div class="bg-white rounded-xl shadow-md p-6 mb-8">
          <h2 class="text-xl font-bold text-purple-800 mb-6">Dados extraídos do seu BI:</h2>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Nome Completo -->
            <div>
              <label class="block text-gray-700 mb-2">Nome completo</label>
              <div class="bg-purple-50 p-3 rounded-lg border border-purple-200">
                {{ extractedData.nomeCompleto || 'Não identificado' }}
              </div>
            </div>

            <!-- Número do BI -->
            <div>
              <label class="block text-gray-700 mb-2">Número do BI</label>
              <div class="bg-purple-50 p-3 rounded-lg border border-purple-200">
                {{ extractedData.numeroBI || 'Não identificado' }}
              </div>
            </div>

            <!-- Filiação (Pai) -->
            <div>
              <label class="block text-gray-700 mb-2">Filiação (Pai)</label>
              <div class="bg-purple-50 p-3 rounded-lg border border-purple-200">
                {{ extractedData.filiacaoPai || 'Não identificado' }}
              </div>
            </div>

            <!-- Filiação (Mãe) -->
            <div>
              <label class="block text-gray-700 mb-2">Filiação (Mãe)</label>
              <div class="bg-purple-50 p-3 rounded-lg border border-purple-200">
                {{ extractedData.filiacaoMae || 'Não identificada' }}
              </div>
            </div>
          </div>

          <div class="mt-4 text-center text-sm text-gray-500">
            <font-awesome-icon icon="info-circle" class="mr-1" />
            Se algum dado estiver incorreto, você pode editar nos campos abaixo
          </div>
        </div>

        <!-- Campos Adicionais -->
        <div class="bg-white rounded-xl shadow-md p-6 mb-8">
          <h2 class="text-xl font-bold text-purple-800 mb-6">Complete suas informações:</h2>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Data de Nascimento -->
            <div>
              <label class="block text-gray-700 mb-2">Data de Nascimento</label>
              <input
                v-model="formData.dataNascimento"
                type="date"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
              />
            </div>

            <!-- Naturalidade -->
            <div>
              <label class="block text-gray-700 mb-2">Natural de</label>
              <input
                v-model="formData.naturalidade"
                type="text"
                placeholder="Ex: Sambizanga"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
              />
            </div>

            <!-- Província -->
            <div>
              <label class="block text-gray-700 mb-2">Província</label>
              <select
                v-model="formData.provincia"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
              >
                <option value="">Selecione sua província</option>
                <option v-for="provincia in provincias" :key="provincia" :value="provincia">
                  {{ provincia }}
                </option>
              </select>
            </div>

            <!-- Sexo -->
            <div>
              <label class="block text-gray-700 mb-2">Sexo</label>
              <div class="flex space-x-4">
                <label class="inline-flex items-center">
                  <input
                    type="radio"
                    v-model="formData.sexo"
                    value="Masculino"
                    class="text-purple-600 focus:ring-purple-500"
                  />
                  <span class="ml-2">Masculino</span>
                </label>
                <label class="inline-flex items-center">
                  <input
                    type="radio"
                    v-model="formData.sexo"
                    value="Feminino"
                    class="text-purple-600 focus:ring-purple-500"
                  />
                  <span class="ml-2">Feminino</span>
                </label>
              </div>
            </div>

            <!-- Estado Civil -->
            <div>
              <label class="block text-gray-700 mb-2">Estado Civil</label>
              <select
                v-model="formData.estadoCivil"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
              >
                <option value="">Selecione seu estado civil</option>
                <option>Solteiro(a)</option>
                <option>Casado(a)</option>
                <option>Divorciado(a)</option>
                <option>Viúvo(a)</option>
              </select>
            </div>

            <!-- Validade do BI -->
            <div>
              <label class="block text-gray-700 mb-2">Validade do BI</label>
              <input
                v-model="formData.validadeBI"
                type="date"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
              />
            </div>

            <!-- Residência -->
            <div class="md:col-span-2">
              <label class="block text-gray-700 mb-2">Residência</label>
              <input
                v-model="formData.residencia"
                type="text"
                placeholder="Ex: Rua Comandante Gika, nº 25, Maianga"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-600 focus:outline-none"
              />
            </div>
          </div>
        </div>

        <!-- Mensagem de Erro -->
        <div v-if="error" class="mb-6 p-4 bg-red-50 text-red-700 rounded-lg text-center">
          <font-awesome-icon icon="exclamation-circle" class="mr-2" />
          {{ error }}
        </div>

        <!-- Botões de Navegação -->
        <div class="flex flex-col sm:flex-row justify-between gap-4">
          <button
            @click="voltarParaUpload"
            class="bg-gray-300 text-gray-700 px-6 py-3 rounded-full font-medium hover:bg-gray-400 transition"
          >
            <font-awesome-icon icon="arrow-left" class="mr-2" /> Voltar
          </button>

          <button
            @click="confirmarDados"
            :disabled="loading"
            class="btn-primary text-white px-8 py-3 rounded-full font-bold text-lg disabled:opacity-70"
          >
            <span v-if="loading">
              <font-awesome-icon icon="spinner" spin class="mr-2" /> Processando...
            </span>
            <span v-else>Confirmar e Avançar</span>
          </button>
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
  name: 'ConfirmData',
  data() {
    return {
      // Dados extraídos do BI (simulados)
      extractedData: {
        nomeCompleto: 'Maria da Conceição Silva',
        numeroBI: '003456789LA045',
        filiacaoPai: 'João Carlos Silva',
        filiacaoMae: 'Ana Maria Silva',
      },

      // Dados do formulário
      formData: {
        dataNascimento: '',
        naturalidade: '',
        provincia: '',
        sexo: '',
        estadoCivil: '',
        residencia: '',
        validadeBI: '',
      },

      // Lista de províncias de Angola
      provincias: [
        'Bengo',
        'Benguela',
        'Bié',
        'Cabinda',
        'Cuando-Cubango',
        'Cuanza-Norte',
        'Cuanza-Sul',
        'Cunene',
        'Huambo',
        'Huíla',
        'Luanda',
        'Lunda-Norte',
        'Lunda-Sul',
        'Malanje',
        'Moxico',
        'Namibe',
        'Uíge',
        'Zaire',
      ],

      error: '',
      loading: false,
    }
  },
  methods: {
    voltarParaUpload() {
      this.$router.push('/upload-bi')
    },
    confirmarDados() {
      // Validar campos essenciais
      if (!this.formData.dataNascimento) {
        this.error = 'Por favor, informe sua data de nascimento.'
        return
      }

      if (!this.formData.naturalidade) {
        this.error = 'Por favor, informe sua naturalidade.'
        return
      }

      if (!this.formData.provincia) {
        this.error = 'Por favor, selecione sua província.'
        return
      }

      if (!this.formData.sexo) {
        this.error = 'Por favor, selecione seu sexo.'
        return
      }

      if (!this.formData.residencia) {
        this.error = 'Por favor, informe seu endereço de residência.'
        return
      }

      if (!this.formData.validadeBI) {
        this.error = 'Por favor, informe a validade do seu BI.'
        return
      }

      // Limpar erro se tudo estiver válido
      this.error = ''
      this.loading = true

      // Simular processamento
      setTimeout(() => {
        this.loading = false
        this.$router.push('/capture-photo')
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

.btn-primary:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(102, 45, 145, 0.25);
}

.btn-primary:disabled {
  background: #c084fc;
  cursor: not-allowed;
}
</style>
