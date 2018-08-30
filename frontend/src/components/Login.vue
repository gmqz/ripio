<template>
    <div id="loginComponent">
        <form class="form-signin">
            <div class="text-center mb-4">
                <img class="mb-2" src="https://ripio-cms-us.s3.amazonaws.com/filer_public/b5/ef/b5efcae0-ade0-44e4-91c3-b3e869ef0b23/logo-ripio-footer.svg" alt="" height="100">
            </div>

            <div class="form-label-group">
                <input id="inputUsername" type="text" class="form-control" name="username" v-model="username" placeholder="Username" required autofocus />
                <label for="inputUsername"><i class="fas fa-user"></i> Username</label>
            </div>

            <div class="form-label-group">
                <input id="inputPassword" type="password" class="form-control" name="password" v-model="password" placeholder="Password" required/>
                <label for="inputPassword"><i class="fas fa-key"></i> Password</label>
            </div>

            <div class="checkbox mb-3">
                <label>
                    <input type="checkbox" value="remember-me"> Remember me
                </label>
            </div>
            <div class="checkbox mb-1 muted">
                <i class="fas fa-user-plus"></i> Si no tiene una cuenta, cree una <router-link to="/newAccount">aqui.</router-link>
            </div>
            <b-button
                variant="primary"
                block
                :disabled="state"
                v-on:click="login()"><i class="fas fa-sign-in-alt"></i> Sign in</b-button>
        </form>
    </div>
</template>

<script>
// import store from '@/store'

export default {
    name: 'Login',
    data () {
        return {
            username: '',
            password: ''
        }
    },
    computed : {
        state () {
            return this.username && this.password ? false : true
        }
    },
    methods: {
        login () {
            let that = this
            this.$store.dispatch('obtainToken', {
                username: this.username,
                password: this.password
            })
                .then(() => this.$router.push('/sys'))
                .catch((error) => {
                    let errorMessage = "Error en la comunicación"
                    if (error.response) {
                        errorMessage = error.response.data.message
                    }
                    that.$swal({
                        toast: true,
                        position: 'top-end',
                        type: 'error',
                        title: error.response.data.message,
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
