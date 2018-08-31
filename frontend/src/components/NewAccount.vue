<template>
    <div id="loginComponent">
        <form class="form-signin">
            <div class="text-center mb-4">
                <img class="mb-2" src="https://ripio-cms-us.s3.amazonaws.com/filer_public/b5/ef/b5efcae0-ade0-44e4-91c3-b3e869ef0b23/logo-ripio-footer.svg" alt="" height="100">
            </div>

            <div class="form-label-group">
                <input id="inputUsername" type="text" class="form-control" name="username" v-model="username" placeholder="Usuario" required autofocus />
                <label for="inputUsername"><i class="fas fa-user-edit"></i> Usuario</label>
            </div>
            <div class="form-label-group">
                <input id="inputFirstname" type="text" class="form-control" name="firstname" v-model="firstname" placeholder="Nombre" required />
                <label for="inputFirstname"><i class="fas fa-user-edit"></i> Nombre</label>
            </div>
            <div class="form-label-group">
                <input id="inputLastname" type="text" class="form-control" name="lastname" v-model="lastname" placeholder="Apellido" required />
                <label for="inputLastname"><i class="fas fa-user-edit"></i> Apellido</label>
            </div>
            <div class="form-label-group">
                <input id="inputEmail" type="email" class="form-control" name="username" v-model="email" placeholder="Username" required />
                <label for="inputEmail"><i class="fas fa-envelope"></i> Email</label>
            </div>
            <div class="form-label-group">
                <input id="inputPassword" type="password" class="form-control" name="password" v-model="password" placeholder="Password" required/>
                <label for="inputPassword"><i class="fas fa-key"></i> Password</label>
            </div>
            <div class="form-label-group">
                <input id="inputFunds" type="number" class="form-control" name="funds" v-model="funds" placeholder="Fondos para comenzar el test" required/>
                <label for="inputFunds"><i class="fas fa-money-bill-wave"></i> Fondos</label>
                <small class="form-text text-muted">Fondos para comenzar el test</small>
            </div>

            <b-button
                variant="primary"
                block
                :disabled="state"
                v-on:click="commit()"><i class="fas fa-user-plus"></i> Crear</b-button>
        </form>
    </div>
</template>

<script>
// import store from '@/store'
import axios from 'axios'
export default {
    name: 'NewAccount',
    data () {
        return {
            username: '',
            firstname: '',
            lastname: '',
            email: '',
            password: '',
            funds: ''
        }
    },
    computed: {
        state () {
            return this.username &&
                this.firstname &&
                this.lastname &&
                this.email &&
                this.funds &&
                this.password
        }
    },
    methods: {
        commit () {
            const store = this.$store
            let that = this
            let payload = {
                username: this.username,
                firstname: this.firstname,
                lastname: this.lastname,
                email: this.email,
                password: this.password,
                funds: this.funds
            }
            axios.post(store.state.endpoints.user, payload, { headers: { Authorization: `Bearer ${store.state.jwt}` } })
                .then((response) => {
                    that.$swal({
                        toast: true,
                        position: 'top-end',
                        type: 'success',
                        title: 'Su registro fue completado!',
                        showConfirmButton: false,
                        timer: 3000
                    })
                    this.$router.push('/login')
                })
                .catch((error) => {
                    let errorMessage = 'Error en la comunicación'
                    if (error.response) {
                        errorMessage = error.response.data.message
                    }
                    that.$swal({
                        toast: true,
                        position: 'top-end',
                        type: 'error',
                        title: errorMessage,
                        showConfirmButton: false,
                        timer: 3000
                    })
                })
        }
    },
    beforeMount () {
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#app {
    width: 100%;
}
.form-signin {
    width: 100%;
    max-width: 420px;
    padding: 15px;
    margin: auto;
}

.form-label-group {
    position: relative;
    margin-bottom: 1rem;
}
.form-label-group > input {
    height: 48px;
}
.form-label-group > input {
    padding: 12px 30px;
}
.form-label-group > label {
    padding: 12px;
}

.form-label-group > label {
    position: absolute;
    top: 0;
    left: 0;
    display: block;
    width: 100%;
    margin-bottom: 0; /* Override default `<label>` margin */
    line-height: 1.5;
    color: #495057;
    border: 1px solid transparent;
    border-radius: .25rem;
    transition: all .1s ease-in-out;
}

.form-label-group input::-webkit-input-placeholder {
    color: transparent;
}

.form-label-group input:-ms-input-placeholder {
    color: transparent;
}

.form-label-group input::-ms-input-placeholder {
    color: transparent;
}

.form-label-group input::-moz-placeholder {
    color: transparent;
}

.form-label-group input::placeholder {
    color: transparent;
}

.form-label-group input:not(:placeholder-shown) {
    padding-top: calc(var(--input-padding-y) + var(--input-padding-y) * (2 / 3));
    padding-bottom: calc(var(--input-padding-y) / 3);
}

.form-label-group input:not(:placeholder-shown) ~ label {
    padding-top: calc(var(--input-padding-y) / 3);
    padding-bottom: calc(var(--input-padding-y) / 3);
    font-size: 11px;
    color: #777;
}
</style>
