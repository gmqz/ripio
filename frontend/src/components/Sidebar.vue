<template>
    <nav class="col-md-2 d-none d-md-block bg-light sidebar">
        <div class="sidebar-sticky">
            <ul class="nav flex-column">
                <li class="nav-item">
                    <a v-bind:class="{ active: current == 'v-dashboard','nav-link': true}" v-on:click="select('v-dashboard')">
                        <i class="fas fa-chart-line"></i>
                        Dashboard <span class="sr-only">(current)</span>
                    </a>
                </li>
                <!-- <li class="nav-item">
                    <a class="nav-link" href="#">
                        <span data-feather="file"></span>
                        Orders
                    </a>
                </li> -->
                <li class="nav-item">
                    <a v-bind:class="{ active: current == 'v-account','nav-link': true}" v-on:click="select('v-account')">
                        <i class="far fa-folder"></i>
                        Cuentas
                    </a>
                </li>
                <li class="nav-item">
                    <a v-bind:class="{ active: current == 'v-transaction','nav-link': true}" v-on:click="select('v-transaction')">
                        <i class="fas fa-exchange-alt"></i>
                        Movimientos
                    </a>
                </li>
                <li class="nav-item">
                    <a v-bind:class="{ active: current == 'v-profile','nav-link': true}" v-on:click="select('v-profile')">
                        <i class="fas fa-user-edit"></i>
                        Perfil
                    </a>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
// import store from '@/store'
export default {
    name: 'Sidebar',
    data () {
        return {
            current: 'v-dashboard'
        }
    },
    methods: {
        select (item) {
            this.$store.dispatch('inspectToken')
                .then((result) => {
                    if (!result) {
                        this.$router.push('/login')
                    }
                })
            this.current = item
            this.$emit('interface', item)
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

/*
 * Sidebar
 */
.nav-item {
    cursor: pointer;
}
.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100; /* Behind the navbar */
  padding: 48px 0 0; /* Height of navbar */
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: .5rem;
  overflow-x: hidden;
  overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
}

@supports ((position: -webkit-sticky) or (position: sticky)) {
  .sidebar-sticky {
    position: -webkit-sticky;
    position: sticky;
  }
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}

.sidebar .nav-link .feather {
  margin-right: 4px;
  color: #999;
}

.sidebar .nav-link.active {
  color: #007bff;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
  color: inherit;
}

.sidebar-heading {
  font-size: .75rem;
  text-transform: uppercase;
}
</style>
