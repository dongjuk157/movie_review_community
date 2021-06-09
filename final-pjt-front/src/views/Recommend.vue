<template>
  <div>
    <h1 class="header">Recommend</h1>
    <div>
      <div class="container">
        <h2>개인 맞춤 영화</h2>
        <MultipleCarousel :movies="personalList" :modalName="'personal'"/>
      </div>
      <div class="container">
        <h2>TOP 10 엄선작</h2>
        <MultipleCarousel :movies="top10list" :modalName="'top10'"/>
      </div>
      <div class="container">
        <h2>유저 선정작</h2>
        <MultipleCarousel :movies="topRateList" :modalName="'topRate'"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MultipleCarousel from '@/components/MultipleCarousel.vue'
export default {
  components:{
    MultipleCarousel,
  },
  methods:{
    top10(){
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/movies/recommend_vote/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`, 
        },
      })
        .then((res)=>{
        this.$store.dispatch('getTop10Movies', res.data)
      }).catch((e)=>{
        console.log(e)
      })
    },
    topRate(){
      const API_KEY = '62a02e776e4bd0a23d54988aadcfde01'
      axios({
        method: 'get',
        url:`https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-KR&page=1`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`, 
        },
      })
        .then((res)=>{
        const movieList = res.data.results.slice(10)
        movieList.forEach((movie) => {
          const tmp = movie.genre_ids.join()
          movie.genre_ids = tmp
          movie['movie_id'] = movie.id
        });
        // console.log(this.movieList)
        
        this.$store.dispatch('getTopRateMovies', movieList)
      }).catch((e)=>{
        console.log(e)
      })
    },
    personal(){
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/movies/recommend_personal/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`, 
        },
      })
        .then((res)=>{
        this.$store.dispatch('getPersonalMovies', res.data)
      }).catch((e)=>{
        console.log(e)
      })
    },
  },
  created(){
    this.top10()
    this.topRate()
    this.personal()
  },
  computed:{
    top10list: {
      get(){
        return this.$store.state.top10list
      },
      set(){},
    },
    topRateList: {
      get(){
        return this.$store.state.topRateList
      },
      set(){},
    },
    personalList: {
      get(){
        return this.$store.state.personalList
      },
      set(){},
      
    },
  }
}
</script>

<style scoped>
h2{
  color:#fff;
  margin-left: 2vh;
  text-align: left;
}
</style>
