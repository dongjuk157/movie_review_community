<template>
  <div class='body'>
    <div class="login-form">
      <div class="container">
        <div class="flux">LOGIN</div>
      </div>
      <form @submit.prevent="onLogin">
        <div class="int-area">
          <label for="id">USER NAME</label>
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
        <div class="btn-area">
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  beforeCreate(){
    document.body.className = 'login'
  },
  data(){
    return {
      credentials: {
        username: '',
        password: '',
      },
    }
  },
  methods:{
    onLogin(){
      const params = {
        method: "POST",
        url: 'http://127.0.0.1:8000/accounts/login/',
        data: this.credentials,
      }
      axios(params)
        .then((res)=>{
          localStorage.setItem('jwt', res.data.token)
          this.$store.dispatch('isLogin')
          this.$router.push({name:'Movies'})
        })
        .catch(()=>{
          alert('비밀번호가 일치하지 않거나 유저가 존재하지 않습니다.')
        })
    }
  },
}
</script>

<style>

</style>