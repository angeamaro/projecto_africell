import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'
import UploadBI from '../views/UploadBI.vue'
import ConfirmData from '../views/ConfirmData.vue'
import CapturePhoto from '../views/CapturePhoto.vue'
import ValidateSMS from '../views/ValidateSMS.vue'
import Success from '../views/Success.vue'
import Error from '../views/Error.vue'
import NotFound from '../views/NotFound.vue' // Página 404

const routes = [
  { path: '/', component: Home },
  { path: '/upload-bi', component: UploadBI },
  { path: '/confirm-data', component: ConfirmData },
  { path: '/capture-photo', component: CapturePhoto },
  { path: '/validate-sms', component: ValidateSMS },
  { path: '/success', component: Success },
  { path: '/error', component: Error },
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound }, // 404
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
