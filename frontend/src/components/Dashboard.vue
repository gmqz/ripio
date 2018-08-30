<template>
    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
        <div class="row">
            <div class="col-sm-6 col-md-4">
                <b-card img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPFdtPyJsQo4LP5Gn_IMdwTipdT1NYM2MUhfAL4YU1__HFYrCg0A"
                        img-alt="Card image"
                        img-top>
                    <div class="text-center" style="margin-top: -180px">
                        <b-img rounded="circle" height="200" blank-color="#777" alt="img"  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2IyAm37DRwmbTkB9j7Vicr_fYKjqmss8Z6W7qmD0ZU_Vad2xn" />

                    </div>
                    <h4 class="text-center">{{ data.lastname }}, {{ data.firstname }}</h4>
                    <h6 class="mb-4 text-center font-italic text-muted">{{ data.email }}</h6>
                    <div class="row">
                        <div class="col-sm-4 text-center m-0" title="Cuentas">
                            <span class="font-weight-bold text-size-lg">{{ data.accounts.length }}</span><br>
                            <i class="far fa-folder fa-lg text-primary"></i>
                        </div>
                        <div class="col-sm-4 text-center m-0 border-left" title="Transacciones">
                            <span class="font-weight-bold text-size-lg">2432</span><br>
                            <i class="fas fa-exchange-alt fa-lg text-warning"></i>
                        </div>
                        <div class="col-sm-4 text-center m-0 border-left" title="Fondos">
                            <span class="font-weight-bold text-size-lg">123k</span><br>
                            <i class="fas fa-money-bill-wave fa-lg text-success"></i>
                        </div>
                    </div>
                </b-card>
            </div>
        </div>

        <canvas class="my-4 w-100" id="myChart" width="900" height="380"></canvas>

        <h2>Section title</h2>
        <div class="table-responsive">
            <table class="table table-striped table-sm">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Header</th>
                        <th>Header</th>
                        <th>Header</th>
                        <th>Header</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1,001</td>
                        <td>Lorem</td>
                        <td>ipsum</td>
                        <td>dolor</td>
                        <td>sit</td>
                    </tr>
                    <tr>
                        <td>1,002</td>
                        <td>amet</td>
                        <td>consectetur</td>
                        <td>adipiscing</td>
                        <td>elit</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </main>
</template>

<script>
// import store from '@/store'
export default {
    name: 'Dashboard',
    data () {
        return {
            data: this.$store.state.user
        }
    },
    methods: {
        // logout () {
        //     console.log(111)
        //     this.$store.dispatch('removeToken')
        //         .then(() => this.$router.push('/login'))
        // }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.text-size-lg {
    font-size: 1rem;
}
</style>
