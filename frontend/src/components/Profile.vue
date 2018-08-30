<template>
    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
        <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
            <h1 class="h2">Profile</h1>
        </div>
        <div class="row">
            <div class="col-md-3 col-lg-3" align="center">
                <img alt="User Pic" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2IyAm37DRwmbTkB9j7Vicr_fYKjqmss8Z6W7qmD0ZU_Vad2xn" class="img-circle img-responsive">
                <button type="button" class="btn btn-link btn-sm p-0"><i class="fas fa-camera"></i> Cambiar</button>
            </div>
            <div class=" col-md-9 col-lg-9 ">
                <table class="table table-user-information">
                    <tbody>
                        <tr>
                            <td class="border-top-0">Username:</td>
                            <td class="border-top-0">{{ data.username }}</td>
                        </tr>
                        <tr>
                            <td>Nombre:</td>
                            <td>{{ data.lastname }}, {{ data.firstname }}</td>
                        </tr>
                        <tr>
                            <td>Email:</td>
                            <td>{{ data.email }}</td>
                        </tr>
                        <tr>
                            <td>Contraseña:</td>
                            <td>********* <button type="button" class="btn btn-link btn-sm p-0">Cambiar</button></td>
                        </tr>
                        <tr>
                            <td>Activo desde:</td>
                            <td>{{ data.createdAt }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </main>
</template>

<script>
// import store from '@/store'
export default {
    name: 'Profile',
    data () {
        return {
            data: this.$store.state.user
        }
    },
    methods: {}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
