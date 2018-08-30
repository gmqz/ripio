import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)
//  return axios.post(`${API_URL}/surveys/`, survey, { headers: { Authorization: `Bearer: ${jwt}` } })

export const store = new Vuex.Store({
    state: {
        jwt: localStorage.getItem('t'),
        endpoints: {
            obtainJWT: 'http://127.0.0.1:8181/api/auth/obtain',
            refreshJWT: 'http://127.0.0.1:8181/api/auth/refresh',
            user: 'http://127.0.0.1:8181/api/user',
            transaction: 'http://127.0.0.1:8181/api/transaction',
            accounts: 'http://127.0.0.1:8181/api/accounts'
        },
        user: {}
    },
    mutations: {
        updateToken (state, payload) {
            state.jwt = payload
            localStorage.setItem('t', payload)
        },
        removeToken (state) {
            localStorage.removeItem('t')
            state.jwt = null
        },
        updateUserData (state, payload) {
            console.log(1)
            state.user = payload
        }
    },
    actions: {
        obtainToken (context, userData) {
            return axios.post(this.state.endpoints.obtainJWT, userData)
                .then((response) => {
                    this.commit('updateToken', response.data.access_token)
                })
                .catch((error) => {
                    throw error
                    //throw new TypeError("Do not use the svg extension")
                })
        },
        refreshToken () {
            const payload = {
                token: this.state.jwt
            }
            return axios.post(this.state.endpoints.refreshJWT, payload)
                .then((response) => {
                    this.commit('updateToken', response.data.access_token)
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        refreshUser () {
            return axios.get(this.state.endpoints.user, { headers: { Authorization: `Bearer ${this.state.jwt}` } })
                .then((response) => {
                    this.commit('updateUserData', response.data)
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        removeToken () {
            this.commit('updateToken', '')
        },
        inspectToken () {
            let jwt = localStorage.getItem('t')
            if (!jwt || jwt.split('.').length < 3) {
                return false
            }
            let data = JSON.parse(atob(jwt.split('.')[1]))
            let exp = new Date(data.exp * 1000) // JS deals with dates in milliseconds since epoch
            let now = new Date()
            return now < exp
        }
    }
})
