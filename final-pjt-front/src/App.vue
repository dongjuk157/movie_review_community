<template>
  <div id="app">
    <div id="nav">
      <span v-if="loginCheck">
        <router-link :to="{name:'Movies'}">Movies</router-link> |
        <router-link :to="{name:'Recommend'}">Recommend</router-link> |
        <router-link :to="{name:'Community'}">Community</router-link> |
        <router-link :to="{name:'MyPage'}">MyPage</router-link> |
        <router-link to="#" @click.native="logout">Logout</router-link>
        <router-link :to="{name:'Movies'}" id="mark">No.1</router-link>
      </span>
      <span v-else>
        <router-link :to="{name:'Signup'}">Signup</router-link> |
        <router-link :to="{name:'Login'}">Login</router-link>
        <router-link :to="{name:'Login'}" id="mark">No.1</router-link>
      </span>
    </div>
    <section id="content">
      <router-view/>
    </section>
    <footer>
      <div class="foot">고동건 github : https://github.com/dongjuk157</div>
      <div class="foot">박선주 github : https://github.com/park-seonju</div>
    </footer>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
export default {
  name:'app',
  methods:{
    logout(){
      localStorage.removeItem('jwt')
      this.$store.dispatch('logout')
      this.$router.push({ name:'Login' })
    },
  },
  computed:{
    ...mapGetters([
      'loginCheck',
    ]),
  },
  created(){
    const API_URL = 'http://127.0.0.1:8000/movies/'
    const params = {
      methods: 'get',
      url: API_URL,
    }
    if (this.$store.state.movies.length===0){
      axios(params)
        .then((res)=>{
          this.$store.dispatch('loadData', res.data)
      }).catch((e)=>{
          console.log(e)
      })
      if (this.loginCheck){
        this.$router.push({name:'Movies'})
      }
    }
    if(this.loginCheck){
      this.$router.push({name:'Movies'})
    }
  },
  mounted(){
    window.addEventListener('resize', ()=>{
      this.$store.dispatch('updateWindowWidth', window.innerWidth)
    })
  }
}
</script>


<style>
@import url('https://fonts.googleapis.com/css?family=Noto+Sans+KR&display=swap');
* {margin:0;padding:0;box-sizing: border-box;}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position:relative
}
#nav {
  padding: 30px;
}

#nav a {
  text-decoration: none;
  font-weight: bold;
  /* color: #2c3e50; */
  color: rgb(120, 120, 120)
}

#nav a.router-link-exact-active {
  /* color: #42b983; */
  color: rgb(190, 0, 0)
}

html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  display: table;
  background-color: black;
}

body {
  overflow: auto;
  min-height: 100vh;
}
.card:focus,
.card:hover {
  transition-delay: 500ms;
  transform: scale(1.2);
  z-index: 1;
}
.card:hover .description{
 width: 100%;
 /* height: 100%; */
 padding: 8px 15px;
 visibility: visible;
 opacity: 0.8; 
 transition-delay: 300ms;
}

.card {
  position: relative;
  display: block;
  flex: 1 1 0px;
  transition: 500ms;
  opacity: 1;
}

.card img{
  display: block;
  max-width: 100%;
}

.card .description{
  position: absolute;
  bottom: 0;
  left: 0;
  background: black;
  color: white;
  opacity: 0;
  visibility: hidden;
  -webkit-transition: visibility 0s, opacity 0.5s linear; 
  transition: visibility 0s, opacity 0.5s linear;
}

@font-face {
  font-family: neon;
  src: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/707108/neon.ttf);
}

.container {
  /* display: table-cell; */
  text-align: center;
  vertical-align: middle;
  /* margin-bottom: 10vh; */
}

.neon {
  font-family: neon;
  color: #FB4264;
  font-size: 9vh;
  line-height: 9vh;
  text-shadow: 0 0 3vw #F40A35;
  margin-bottom: 5vh;
}

.flux {
  font-family: neon;
  color: #426DFB;
  font-size: 9vh;
  line-height: 9vh;
  text-shadow: 0 0 3vw #2356FF;
  margin-bottom: 5vh;
}

.neon {
  margin-bottom:5vh;
  animation: neon 1s ease infinite;
  -moz-animation: neon 1s ease infinite;
  -webkit-animation: neon 1s ease infinite;
}

@keyframes neon {
  0%,
  100% {
    text-shadow: 0 0 1vw #FA1C16, 0 0 3vw #FA1C16, 0 0 10vw #FA1C16, 0 0 10vw #FA1C16, 0 0 .4vw #FED128, .5vw .5vw .1vw #806914;
    color: #FED128;
  }
  50% {
    text-shadow: 0 0 .5vw #800E0B, 0 0 1.5vw #800E0B, 0 0 5vw #800E0B, 0 0 5vw #800E0B, 0 0 .2vw #800E0B, .5vw .5vw .1vw #40340A;
    color: #806914;
  }
}

.flux {
  animation: flux 2s linear infinite;
  -moz-animation: flux 2s linear infinite;
  -webkit-animation: flux 2s linear infinite;
  -o-animation: flux 2s linear infinite;
}

@keyframes flux {
  0%,
  100% {
    text-shadow: 0 0 1vw #1041FF, 0 0 3vw #1041FF, 0 0 10vw #1041FF, 0 0 10vw #1041FF, 0 0 .4vw #8BFDFE, .5vw .5vw .1vw #147280;
    color: #28D7FE;
  }
  50% {
    text-shadow: 0 0 .5vw #082180, 0 0 1.5vw #082180, 0 0 5vw #082180, 0 0 5vw #082180, 0 0 .2vw #082180, .5vw .5vw .1vw #0A3940;
    color: #146C80;
  }
}
/* footer */
footer{
  text-align: end;
  color:silver;
  margin-top:1vh;
  margin-right:40px;
  
}
#content{
  min-height: 100%;
}

/* signup login form  */
body.signup,
body.login{
  background: url("./assets/background3.jpg") no-repeat center;
  background-size:cover;
  background-attachment: fixed;
}

.body{
  font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}
.login-form {
  position: relative; 
  z-index: 2;
  padding: 7vh;
  background: #fff;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 2vh;
}
.int-area{
  width: 40vh; 
  position: relative;
  margin-top: 2vh;
  font-size: 18px; color:#eee;
}
.int-area label{
  position: absolute; 
  bottom: 4vh;
  transition: top .5s ease;
  padding: 1vh 0;
}
.int-area input{
  width:100%;
  padding: 1vh 0.5vh;
  margin-bottom: 1vh;
  background-color: transparent;
  border:none;
  border-bottom: 1px solid #fff;
  outline: none;
  color: #fff;
}
.btn-area{
  margin-top:30px;
}
.btn-area button{
  width:100%;height: 50px;
  background: #166cea;
  color: #fff;
  font-size:20px;
  border:none;
  border-radius: 25px;
}


@font-face {
  font-family: neon;
  src: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/707108/neon.ttf);
}

#mark {
  /* margin-bottom:5vh; */
  animation: neon 1s ease infinite;
  -moz-animation: neon 1s ease infinite;
  -webkit-animation: neon 1s ease infinite;

  position: fixed;
  top:0;
  right:0;
  font-family: neon;
  color: #FB4264;
  font-size: 4vh;
  text-shadow: 0 0 3vw #F40A35;
}

@keyframes mark {
  0%,
  100% {
    text-shadow: 0 0 1vw #FA1C16, 0 0 3vw #FA1C16, 0 0 10vw #FA1C16, 0 0 10vw #FA1C16, 0 0 .4vw #FED128, .5vw .5vw .1vw #806914;
    color: #FED128;
  }
  50% {
    text-shadow: 0 0 .5vw #800E0B, 0 0 1.5vw #800E0B, 0 0 5vw #800E0B, 0 0 5vw #800E0B, 0 0 .2vw #800E0B, .5vw .5vw .1vw #40340A;
    color: #806914;
  }
}

/*////////////////////////////////*/
</style>
