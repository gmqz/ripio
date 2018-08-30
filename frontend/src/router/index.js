import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Sys from '@/components/Sys'
import NewAccount from '@/components/NewAccount'
import {store} from '@/store'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home
        },
        {
            path: '/login',
            name: 'Login',
            component: Login,
            beforeEnter (to, from, next) {
                store.dispatch('inspectToken')
                    .then((result) => {
                        if (result) {
                            next('/sys')
                        } else {
                            next()
                        }
                    })
            }
        },
        {
            path: '/newAccount',
            name: 'NewAccount',
            component: NewAccount,
            beforeEnter (to, from, next) {
                store.dispatch('inspectToken')
                    .then((result) => {
                        if (result) {
                            next('/sys')
                        } else {
                            next()
                        }
                    })
            }
        },
        {
            path: '/sys',
            name: 'Sys',
            component: Sys,
            beforeEnter (to, from, next) {
                store.dispatch('inspectToken')
                    .then((result) => {
                        if (result) {
                            next()
                        } else {
                            next('/login')
                        }
                    })
            }
        }
    ]
})
