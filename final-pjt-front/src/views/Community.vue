<template>
  <div class="container">
    <h1 class="header">Community</h1>
    <div class="overflow-auto">
    <ul 
      id="my-list"
    >
      <li
        v-for="review in SomeReviews" 
        :key="review.id"
        @click="onClick(review)"
        class="ultag"
      >
        <img
          :src="'https://image.tmdb.org/t/p/w500/' + movie[review.movie].poster_path"
          alt=""
          width="180"
          class="clickcursor d-none d-md-block"
        >
        <div class="content clickcursor">
          <div class="review_title title_common">
            <div class="rt">{{ review.title }}</div>
            <div class="rvscore" v-if="review.score === 5">★★★★★</div>
            <div class="rvscore" v-if="review.score === 4">★★★★☆</div>
            <div class="rvscore" v-if="review.score === 3">★★★☆☆</div>
            <div class="rvscore" v-if="review.score === 2">★★☆☆☆</div>
            <div class="rvscore" v-if="review.score === 1">★☆☆☆☆</div>
            <div class="rvscore" v-if="review.score === 0">☆☆☆☆☆</div>
          </div>    
          <div class="m_title title_common">
            {{ movie[review.movie].title }}
          </div>
        </div>
      </li>
    </ul>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-list"
        class="page"
      ></b-pagination>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  data(){
    return {
      perPage:5,
      currentPage:1,
    }
  },
  name: 'Community',
  props:{},
  methods:{
    onClick(review){
      this.$store.state.selectReview = review
      this.$router.push({name: 'ReviewDetail'})
    }
  },
  computed:{
    reviews(){
      return this.$store.state.reviews
    },
    movie(){
      return this.$store.state.movies
    },
    rows() {
        return this.$store.state.reviews.length
    },
    SomeReviews(){
      return this.reviews.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage
      )
    }
  },
  created(){
    const token = localStorage.getItem('jwt')
    const URL =  'http://127.0.0.1:8000/review/'
    const params = {
      method:'get',
      url: URL,
      headers: {
        Authorization: `JWT ${token}`, 
      },
    }
    axios(params)
      .then((res)=>{
        this.$store.dispatch('getReviews', res.data)
      })
      .catch((e)=>{
        console.log(e)
      })
  },
}
</script>

<style >
.ultag{
  display:flex;
  margin: 2vh;
  /* margin: 20px; */
  /* max-width: 80%; */
}
.page{
  justify-content: center;
}
.rt{
  padding-top: 30px;
  font-size:40px;
}
.score{
  font-size:22px;
}
.clickcursor{
  cursor: pointer;
  justify-content: center;
  align-items: center;
}
.title_common{
  display: flex;
  flex-direction: column;
  color:#fff;
  height: 50%;
  justify-content: center;
  align-items: flex-start;
}
.review_title{
  margin-top: 10px;
  font-size: 25px;
}
.m_title{
  font-size: 20px;
}
.content{
  width:100%;
  margin-right: 30px;
  margin-left: 20px;
  padding-left: 1vh;
  align-items:center;
  background-color: rgba(255,255,255,0.1);
}
.overflow-auto{
  /* padding-left:10vh;
  padding-right:10vh; */
  
}
.rvscore{
  font-size:40px;
  content: "★";
  color: gold;
  text-shadow: 0 0 1px #333;
}
</style>