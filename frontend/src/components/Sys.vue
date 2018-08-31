<template>
    <div>
        <nav class="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow">
            <img class="col-sm-3 col-md-2 mr-0" src="https://ripio-cms-us.s3.amazonaws.com/filer_public/80/d7/80d76109-a560-446c-9385-d6d911168dbe/logo-ripio-white.svg" alt="" height="40">
            <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
            <ul class="navbar-nav px-3">
                <li class="nav-item text-nowrap">
                    <a class="nav-link" v-on:click="logout()"><i class="fas fa-sign-out-alt"></i> Sign out</a>
                </li>
            </ul>
        </nav>

        <div class="container-fluid">
            <div class="row">
                <v-sidebar @interface="currentOptionComponent = $event"></v-sidebar>
                <!-- <v-dashboard></v-dashboard> -->
                <component v-bind:is="currentOptionComponent">
                    sadasd
                </component>
            </div>
        </div>
    </div>
</template>

<script>
// import store from '@/store'
import Vue from 'vue'
import Sidebar from '@/components/Sidebar'
import Dashboard from '@/components/Dashboard'
import Profile from '@/components/Profile'
import Account from '@/components/Account'
import Transaction from '@/components/Transaction'
Vue.component('v-loading', {
    template: '<main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4 text-center mt-5"><i class="fas fa-spinner fa-spin fa-5x mt-5"></i></main>'
})

export default {
    name: 'App',
    data () {
        return {
            currentOptionComponent: 'v-loading'
        }
    },
    components: {
        'v-sidebar': Sidebar,
        'v-dashboard': Dashboard,
        'v-profile': Profile,
        'v-account': Account,
        'v-transaction': Transaction
    },
    mounted: function () {
        this.$store.dispatch('refreshUser')
            .then(() => { this.currentOptionComponent = 'v-dashboard' })
    },
    methods: {
        logout () {
            this.$store.dispatch('removeToken')
                .then(() => { this.$router.push('/login') })
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
/*
 * Content
 */

[role="main"] {
  padding-top: 48px; /* Space for fixed navbar */
}

/*
 * Navbar
 */
.nav-link {
    cursor: pointer;
}
.navbar-brand {
  padding-top: .75rem;
  padding-bottom: .75rem;
  font-size: 1rem;
  background-color: rgba(0, 0, 0, .25);
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .25);
}

.navbar .form-control {
  padding: .75rem 1rem;
  border-width: 0;
  border-radius: 0;
}

.form-control-dark {
  color: #fff;
  background-color: rgba(255, 255, 255, .1);
  border-color: rgba(255, 255, 255, .1);
}

.form-control-dark:focus {
  border-color: transparent;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, .25);
}

/*
 * Utilities
 */

.border-top { border-top: 1px solid #e5e5e5; }
.border-bottom { border-bottom: 1px solid #e5e5e5; }
</style>
