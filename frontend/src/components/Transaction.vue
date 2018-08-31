<template>
    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
        <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
            <h1 class="h2">Movimientos</h1>
        </div>

        <div class="row">
            <div class="col-xs-12 col-sm-6 col-md-4">
                <b-card border-variant="primary"
                        header="<i class='fas fa-exchange-alt'></i> Nueva transferencia">
                    <b-form-group
                          id="origin"
                          description="Seleccione cuenta origen."
                          label="Origen"
                          label-for="origin">
                        <b-form-select v-model="origin" :options="possibleOrigins" class="" />
                        <div class="funds"><i class="fas fa-dollar-sign"></i> <small>{{ currentBalance }}</small></div>
                    </b-form-group>

                    <b-form-group
                          id="target"
                          description="Seleccione cuenta destino."
                          label="Destino"
                          label-for="target">
                        <b-form-select v-model="target" :options="possibleTargets" class="" />
                    </b-form-group>

                    <b-form-group
                          id="fieldset1"
                          description="Monto de la operación"
                          type="number"
                          label="Monto"
                          label-for="input1"
                          :invalid-feedback="invalidFeedback"
                          :state="state">
                        <b-form-input id="input1" :state="state" v-model.trim="value"></b-form-input>
                    </b-form-group>

                    <b-button
                        variant="primary"
                        block
                        :disabled="state == false"
                        v-on:click="commit()"><i class="fas fa-check-circle"></i> Enviar</b-button>
                    <!-- <button class="btn btn-primary btn-block" type="button" v-on:click="commit()"><i class="fas fa-check-circle"></i> Enviar</button> -->
                </b-card>
            </div>
            <div class="col-xs-12 col-sm-6 col-md-8">
                <b-card border-variant="warning"
                        no-body
                        header="<i class='fas fa-exchange-alt'></i> Ultimos movimientos">
                    <b-card-body class="mp-0">
                        <div class="table-responsive">
                            <table class="table table-striped table-sm m-0 p-0">
                                <thead>
                                    <tr>
                                        <th class="text-center">#</th>
                                        <th class="text-center">Fecha</th>
                                        <th class="text-center">Referencia</th>
                                        <th class="text-center">Monto</th>
                                        <th class="text-center">Saldo</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="move in currentAccountMoves" :key="move.id">
                                        <td class="text-center align-middle" v-html="move.icon">{{ move.icon }}</td>
                                        <td class="text-center align-middle" v-html="move.createdAt">{{ move.createdAt }}</td>
                                        <td class="align-middle">{{ move.reference }}</td>
                                        <td class="text-center align-middle">{{ move.value }}</td>
                                        <td class="text-center align-middle">{{ move.balance }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </b-card-body>
                </b-card>
            </div>
        </div>
    </main>
</template>

<script>
// import store from '@/store'
import axios from 'axios'
export default {
    name: 'Transaction',
    created: function () {
        let that = this
        axios.get(this.$store.state.endpoints.accounts, { headers: { Authorization: `Bearer ${this.$store.state.jwt}` } })
            .then((response) => {
                that.possibleTargets = response.data.map((item) => {
                    return {
                        value: item.id,
                        text: item.description
                    }
                })
            })
    },
    computed: {
        state () {
            let origin = this.origin
            let aux = this.myAccounts.find((item) => item.id === origin)
            this.value = parseFloat(this.value)
            this.currentBalance = aux ? aux.balance : 0

            return this.value > 0 &&
                this.currentBalance >= this.value &&
                this.origin &&
                this.target &&
                this.target !== this.origin
        },
        invalidFeedback () {
            if (!this.origin) {
                return 'Debe seleccionar una cuenta origen'
            } else if (!this.target) {
                return 'Debe seleccionar una cuenta destino'
            } else if (this.target === this.origin) {
                return 'La cuentas origen y destino no pueden ser la misma'
            } else if (parseFloat(this.value) === 0) {
                return 'Ingrese un monto'
            } else {
                return 'Saldo insuficiente'
            }
        },
        possibleOrigins () {
            return this.$store.state.user.accounts.map((item) => {
                return {
                    value: item.id,
                    text: item.description
                }
            })
        },

        myAccounts () {
            return this.$store.state.user.accounts
        },
        currentAccountMoves () {
            if (this.origin) {
                let origin = this.origin
                let aux = this.myAccounts.find((item) => item.id === origin)
                return aux.transactions.map((item) => {
                    item.createdAt = item.createdAt.replace(' ', '<br><small>') + '</small>'
                    if (item.target.id === origin) {
                        item.icon = '<i class="fas fa-long-arrow-alt-right text-success"></i>'
                        item.reference = item.origin.description
                        item.balance = item.targetBalance
                    } else {
                        item.icon = '<i class="fas fa-long-arrow-alt-left text-danger"></i>'
                        item.reference = item.target.description
                        item.balance = item.originBalance
                    }
                    return item
                }).reverse()
            }
            return []
        }
    },
    data () {
        return {
            origin: '',
            target: '',
            currentBalance: 0,
            value: 0,
            possibleTargets: []
        }
    },
    methods: {
        commit () {
            let payload = {
                origin: this.origin,
                target: this.target,
                value: this.value
            }
            const store = this.$store
            let that = this
            axios.post(store.state.endpoints.transaction, payload, { headers: { Authorization: `Bearer ${store.state.jwt}` } })
                .then((response) => {
                    that.$swal({
                        toast: true,
                        position: 'top-end',
                        type: 'success',
                        title: 'Su transferencia fue completada!',
                        showConfirmButton: false,
                        timer: 3000
                    })
                    store.dispatch('refreshUser')
                        .then(() => console.log(store.state.user))
                })
                .catch((error) => {
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
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.funds {
    position: absolute;
    right: 25px;
}
</style>
