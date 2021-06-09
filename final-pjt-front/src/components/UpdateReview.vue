<template>
  <div class="container">
    <form>
      <div class="total">
        <p class="mv_title">영화: {{ movie.title }}</p>
        <p><label for="title">제목</label></p>
        <p><input type="text" id="title" style="width:80%; padding:10px;" v-model="title"></p>
        <p><label for="content">리뷰 작성</label></p>
        <p><textarea type="text" id="content" v-model="content" style="width:80%; resize:none;" rows=15px></textarea></p>
        <fieldset class="star_button">
          <p class="scoretext">평점 : </p>
          <span class="star-cb-group" >
            <input type="radio" id="rating-5" name="rating" value="5" v-model="score" checked="checked"/>
            <label for="rating-5">5</label>
            <input type="radio" id="rating-4" name="rating" value="4" v-model="score"/>
            <label for="rating-4">4</label>
            <input type="radio" id="rating-3" name="rating" value="3" v-model="score"/>
            <label for="rating-3">3</label>
            <input type="radio" id="rating-2" name="rating" value="2" v-model="score"/>
            <label for="rating-2">2</label>
            <input type="radio" id="rating-1" name="rating" value="1" v-model="score"/>
            <label for="rating-1">1</label>
            <input type="radio" id="rating-0" name="rating" value="0" v-model="score" class="star-cb-clear" />
            <label for="rating-0">0</label>
          </span>
          <button class="btn btn-primary createbtn" @click.prevent="onClick">작성</button>   
        </fieldset>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateReview',
  data(){
    return {
      title: '',
      content: '',
      score: '',
    }
  },
  created(){
    this.title = this.selectReview.title
    this.content = this.selectReview.content
    this.score = this.selectReview.score
  },
  computed:{
    selectReview(){
      return this.$store.state.selectReview
    },
    movie(){
      return this.$store.state.movies[this.selectReview.movie]
    },
    movieId(){
      return this.$store.state.selectMovie.movie_id
    },
    posterPath(){
      return 'https://image.tmdb.org/t/p/w500/' + this.movie.poster_path
    },
  },
  methods:{
    onClick(){
      const token = localStorage.getItem('jwt')
      const data = {
        title: this.title,
        content: this.content,
        score: this.score,
      }
      const movie_id = this.movie.movie_id
      const review_id = this.selectReview.id

      const URL =  `http://127.0.0.1:8000/review/${movie_id}/${review_id}/`
      const params = {
        method: 'PUT',
        url: URL,
        data: data,
        headers: {
          Authorization: `JWT ${token}`, 
        },
      }
      axios(params)
        .then((res)=>{
          const review = res.data
          review['movie'] -= 1
          this.$store.state.selectReview = review
          this.$router.push({name:'ReviewDetail'})
        })
        .catch((e)=>{
          console.log(e)
        })
    },
  },
}
</script>

<style scoped>
.mv_title{
  font-size:30px;
}
textarea{
  border-radius: 20px;
  padding:10px;
}
.star_button{
  display: flex;
  justify-content: flex-end;
  margin-right:95px;
}
.createbtn{
  margin-left:20px;
}
.scoretext{
  margin-top:25px;
  margin-right:10px;
}
.star-cb-group {
  font-size: 0;
  unicode-bidi: bidi-override;
  direction: rtl;
}
.star-cb-group * {
  font-size: 1rem;
}
.star-cb-group > input {
  display: none;
}
.star-cb-group > input + label {
  display: inline-block;
  overflow: hidden;
  width: 1em;
  white-space: nowrap;
  cursor: pointer;
  font-size:40px;
}
.star-cb-group > input + label:before {
  display: inline-block;
  content: "☆";
  color: #888;
}
.star-cb-group > input:checked ~ label:before, .star-cb-group > input + label:hover ~ label:before, .star-cb-group > input + label:hover:before {
  content: "★";
  color: gold;
  text-shadow: 0 0 1px #333;
}
.star-cb-group > .star-cb-clear + label {
  text-indent: -9999px;
  width: .5em;
  margin-left: -.5em;
}
.star-cb-group > .star-cb-clear + label:before {
  width: .5em;
}
.star-cb-group:hover > input + label:before {
  content: "☆";
  color: #888;
  text-shadow: none;
}
.star-cb-group:hover > input + label:hover ~ label:before, .star-cb-group:hover > input + label:hover:before {
  content: "★";
  color: gold;
  text-shadow: 0 0 1px #333;
}
</style>