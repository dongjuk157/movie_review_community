<template>
  <div class="container">
    <h1 class="header">My Page</h1>
    <div class="mytotal">
      <div class="total mypagetotal row">
        <div class="bbig col-12 col-lg-6">
          <span class="reviewcomment">작성 리뷰</span>
          <ul v-for="review in myReviews" :key="review.id" class="write_review_comment">
            <a href="#" @click.prevent="moveReview(review.id)">
              {{review.title}}
            </a>
            <!-- <button class="btn btn-primary btn-sm originSee" @click="">원문 보기</button> -->
          </ul>
        </div>
        <div class="bbig col-12 col-lg-6">
          <span class="reviewcomment">작성 댓글</span>
          <ul v-for="comment in myComments" :key="comment.id" class="write_review_comment">
            <a href="#" @click.prevent="moveReview(comment.review)">
              {{ comment.content }}
            </a>
            <!-- <button class="btn btn-primary btn-sm originSee" @click="">원문 보기</button> -->
          </ul>
        </div>
      </div>
      <div class="like_movies">
        <h2>좋아요 누른 영화</h2>
        <MultipleCarousel :movies="myMovies" :modalName="'myPage'"/>
      </div>
    </div>
  </div>
</template>

<script>
import MultipleCarousel from '@/components/MultipleCarousel.vue'
import axios from 'axios'
export default {
  components:{
    MultipleCarousel
  },
  data(){
    return {
      myReviews:[],
      myComments:[],
    }
  },
  methods:{
    getProfile(){
      const params = {
        method: 'get',
        url:`http://127.0.0.1:8000/accounts/profile/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`, 
        },
      }
      axios(params)
        .then((res)=>{
        this.myReviews = res.data.reviews
        this.myComments = res.data['comments']
        this.$store.dispatch('getMyPageMovies', res.data['like_movies'])
      }).catch((e)=>{
        console.log(e)
      })
    },
    moveReview(comment_review){
      const params = {
        method: 'get',
        url:`http://127.0.0.1:8000/review/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`, 
        },
      }
      axios(params)
        .then((res)=>{
        res.data.forEach(review => {
          if(review.id===comment_review){
            review.movie-=1
            this.$store.state.selectReview = review
            this.$router.push({name: 'ReviewDetail'})
          }
        });
      }).catch((e)=>{
        console.log(e)
      })
    },
  },
  computed:{
    myMovies(){
      return this.$store.getters.getMyPageMovies
    },
  },
  created(){
    this.getProfile()
  },
}
</script>

<style>
h2{
  color:#fff;
}
.like_movies{
  margin-top:30px;
}
.header{
  color: rgb(202, 201, 202);
  font-size:50px;
  margin: 30px;
}
.reviewcomment{
  font-size: 25px;
  margin-top: 1vh;
}
.write_review_comment{
  display: flex;
  margin-top:25px;
}
.mypagetotal{
  display: flex;
  flex-direction: row;
}
.bbig{
  display: flex;
  flex-direction: column;
  /* width:50%; */
}
.bbig a{
  color: #fff;
}
.bbig a:hover{
  color: #ddd;
}

.originSee{
  margin-left: 15px;
}
</style>