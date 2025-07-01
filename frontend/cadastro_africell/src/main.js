import './assets/main.css'


import { createApp } from 'vue'
import { createPinia } from 'pinia'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faUserSecret, faShieldAlt, faIdCard, faSms, faLock, faFaceSmile, faTimes, faBalanceScale } from '@fortawesome/free-solid-svg-icons'

// Se quiser marcas (ex: faGithub), importe também:
import { faGithub } from '@fortawesome/free-brands-svg-icons'

// Adiciona os ícones à biblioteca
library.add(faUserSecret, faShieldAlt, faIdCard, faSms, faLock, faFaceSmile, faTimes, faGithub, faBalanceScale)

import App from './App.vue'
import router from './router'

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(createPinia())
app.use(router)

app.mount('#app')
