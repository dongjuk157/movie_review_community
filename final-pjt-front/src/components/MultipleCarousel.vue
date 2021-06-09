<template>
  <div class="slide-container container">
    <div class="row m-2 p-2">
      <!-- carousle(slide) 구현 -->
      <div v-for="(movie, idx) in computedMovies" :key="idx" class="col">
        <Card :movie="movie" :modalName="modalName"/>
      </div>
    </div>
    <span class="carousel-control-prev-icon slide-btn slide-btn-left" @click="clickSlideArrow('left')"></span>
    <span class="carousel-control-next-icon slide-btn slide-btn-right" @click="clickSlideArrow('right')"></span>
  </div>
</template>

<script>
import Card from './Card.vue'
export default {
  components: { Card },
  name:'MultipleCarousel',
  props:{
    modalName:{
      tpye: String,
    },
  },
  data () {
    return {
        slide: 0,
        sliding: null,
        current: 0,
    }
  },
  computed:{
    movieLength(){
      return this.movies.length
    },
    moviePosters(){
      const list = []
      this.movies.forEach((movie)=>{
        list.push("https://image.tmdb.org/t/p/w500/" + movie.poster_path)
      })
      return list
    },
    movies(){
      let movieList = []
      if (this.modalName === 'personal'){
        movieList = this.$store.getters.getPersonalList
      }
      else if(this.modalName === 'top10'){
        movieList = this.$store.getters.getTop10list
      }
      else if(this.modalName === 'topRate'){
        movieList = this.$store.getters.getTopRateList
      }
      else if (this.modalName ==='myPage'){
        movieList = this.$store.getters.getMyPageMovies
      }
      return movieList
    },
    computedMovies(){
      // console.log(this.$store.state.windowWidth)
      let numOfCard = 0
      if (this.$store.state.windowWidth < 576){
        numOfCard = 1
      }
      else if (this.$store.state.windowWidth < 768){
        numOfCard = 2
      }
      else if (this.$store.state.windowWidth < 992){
        numOfCard = 3
      }
      else {
        numOfCard = 4
      }

      const ret = Array()
      for (let i = this.current; i < this.current + numOfCard; i++) {
        if (this.movies[i]){
          ret.push(this.movies[i])
        }
      }
      return ret
    },
  },
  methods: {
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    },
    clickSlideArrow(dir){
      let numOfCard = 0
      if (this.$store.state.windowWidth < 576){
        numOfCard = 1
      }
      else if (this.$store.state.windowWidth < 768){
        numOfCard = 2
      }
      else if (this.$store.state.windowWidth < 992){
        numOfCard = 3
      }
      else {
        numOfCard = 4
      }
      if (this.movieLength < numOfCard + 1) {
        // card 개수보다 작거나 같은 경우 동작하지 않게 설정
        return
      }
      if (dir==='left') this.current -= 1
      else              this.current += 1        

      if (this.current >= this.movieLength - (numOfCard - 1)) this.current = 0
      else if (this.current < 0)                this.current = this.movieLength - numOfCard
    }
  },
}
</script>

<style >
.slide-container {
  position: relative;
}
.slide-btn{
  position: absolute;
  top: 40%;
  opacity: 70%;
}
.slide-btn:hover{
  cursor: pointer;
  opacity: 100%;
}
.slide-btn-left{
  left: 0;
}
.slide-btn-right{
  right: 0;
}
</style>
