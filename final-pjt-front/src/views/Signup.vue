<template>
  <div class="body">  
    <div class="login-form">
      <div class="container">
        <div class="neon">Signup</div>
      </div>
      <form @submit.prevent="onSignup">
        <div class="int-area">
          <label for="id">USERNAME</label>
          <input 
            type="text"
            v-model="credentials.username"
            name="id"
            id="id"
            autocomplete="off"
            required
          >
        </div>
        <div class="int-area">
          <label for="pw">PASSWORD</label>
          <input
            type="password"
            v-model="credentials.password"
            name="pw"
            id="pw"
            autocomplete="off"
            required
          >
        </div>
        <div class="int-area">
          <label for="passwordConfirmation">PASSWORD CHECK</label>
          <input
            type="password"
            v-model="credentials.passwordConfirmation"
            name="passwordConfirmation"
            id="passwordConfirmation"
            autocomplete="off"
            required
          >
        </div>
        <div  class="btn-area">
        <button type="submit">Sign Up</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  beforeCreate(){
  document.body.className = 'signup'
  },
  name: 'Signup',
  data(){
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      },
    }
  },
  methods:{
    onSignup(){
      const params = {
        method: "POST",
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      }
      axios(params)
        .then(()=>{
          this.$router.push({name:'Login'})
        })
        .catch((e)=>{
          for (const [key, value] of Object.entries(e.response.data)){
            alert(`${key}: ${value}`)
          }
        })
    }
  }
}
</script>

<style>

</style>