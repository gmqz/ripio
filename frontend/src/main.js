// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// main.js
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
// import jwt_decode from 'jwt-decode'
import BootstrapVue from 'bootstrap-vue'
import { store } from '@/store'
import VueSweetalert2 from 'vue-sweetalert2'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(VueSweetalert2)
/* eslint-disable no-new */

new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>',
    store
})
