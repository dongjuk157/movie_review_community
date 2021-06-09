<template>
  <div class="container">
    <div class=total>
      <div class="title">{{review.title}}<span class="mv_score">{{ reviewScore }}</span></div>
      <div class=" movie_title">
        <span class="fs-4">영화: {{movieTitle}}</span>
        <div>
          <span>
            작성자: {{review.username}}
          </span>
          <span>
            / 작성시간: {{ review.created_at.slice(0, 10) }}
          </span>
        </div>
      </div>
      
      <div class="rv_content">{{review.content}}</div>

      <div v-if="review.user === user" class="buttons">
        <button class="btn btn-outline-success update" @click="onUpdate">수정</button>
        <button class="btn btn-outline-danger delete" @click="onDelete">삭제</button>
      </div>

      <div class="comment_input">
        <div class="c-text">댓글</div>
        <div class="in-line">
          <input
            class="detail_input"
            type="text"
            name="name"
            v-model="comment"
            @keyup.enter="commentSubmit"
            placeholder="댓글을 남겨보세요."
            style="padding:10px;">
            <button type="button" @click="commentSubmit" class="button" style="color:white">등록</button>
        </div>
      </div>
        <div class="comment_total">
          <div class="comment" v-for="comment in comments" :key="comment.id">
            <span>{{comment.username}}: </span>
            <span>{{comment.content}}</span>
            <div class="d-inline" v-if="comment.user===user">
              <button class="btn btn-outline-primary btn-sm comment_update" @click="commentUpdate(comment.id)">수정</button>
              <button class="btn btn-outline-danger btn-sm comment_delete" @click="commentDelete(comment.id)">삭제</button>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  created(){
    this.updateComment()
  },
  data(){
    return {
      comment:'',
      comments: [],
    }
  },
  computed:{
    review(){
      return this.$store.state.selectReview
    },
    movieTitle(){
      const movie_id = this.review.movie
      const movie_info = this.$store.state.movies[movie_id]
      return movie_info.title
    },
    movie(){
      return this.$store.state.movies[this.review.movie]
    },
    user(){
      return  this.$store.state.userId
    },
    reviewScore(){
      let rate = ''
      for (let index = 0; index < this.review.score; index++) {
        rate += '★'
      }

      for (let index = 0; index < 5 - this.review.score; index++) {
        rate += '☆'
      }
      return rate
    }
  },
  methods:{
    onUpdate(){
      this.$router.push({name:'UpdateReview'})
    },
    onDelete(){
      const review_id = this.review.id
      const author = this.review.user
      const movie_id = this.movie.movie_id      
      const token = localStorage.getItem('jwt')
      if (author === this.$store.state.userId){
        const URL = `http://127.0.0.1:8000/review/${movie_id}/${review_id}/`
        const params = {
          method: 'DELETE',
          url: URL,
          headers: {
            Authorization: `JWT ${token}`, 
          },
        }
        axios(params)
          .then(()=>{
            this.$router.push({name:'Community'})
        }).catch((e)=>{
          console.log(e)
        })
      }
    },
    commentSubmit(){
      const review_id = this.review.id
      const token = localStorage.getItem('jwt')
      const URL = `http://127.0.0.1:8000/review/comment/${review_id}/`
      const data = {
        content: this.comment,
      }
      const params = {
        method: 'POST',
        url: URL,
        data: data,
        headers: {
          Authorization: `JWT ${token}`, 
        },
      }
      axios(params)
        .then(()=>{
          this.comment = ''
          this.updateComment()
      })
      .catch((e)=>{
        console.log(e)
      })
    },
    updateComment(){
      const review_id = this.review.id
      const token = localStorage.getItem('jwt')
      const URL = `http://127.0.0.1:8000/review/comment/${review_id}`
      const params = {
        method: 'GET',
        url: URL,
        headers: {
          Authorization: `JWT ${token}`, 
        },
      }
      axios(params)
        .then((res)=>{
          this.comments = res.data
      }).catch((e)=>{
        console.log(e)
      })
    },
    commentDelete(commentId){
      const review_id = this.review.id
      const comment_id = commentId
      const token = localStorage.getItem('jwt')
      const URL = `http://127.0.0.1:8000/review/comment/${review_id}/${comment_id}/`
      const params = {
        method: 'DELETE',
        url: URL,
        headers: {
          Authorization: `JWT ${token}`, 
        },
      }
      axios(params)
        .then(()=>{
          this.updateComment()
      }).catch((e)=>{
        console.log(e)
      })
    },
    commentUpdate(commentId){
      const parent = event.target.parentNode.parentNode
      if (parent.childNodes[1].tagName==="INPUT"){
        const textboxValue = parent.childNodes[1].value
        const review_id = this.review.id
        const comment_id = commentId
        const token = localStorage.getItem('jwt')
        const URL = `http://127.0.0.1:8000/review/comment/${review_id}/${comment_id}/`
        const data = {
          content: textboxValue,
        }
        const params = {
          method: 'PUT',
          url: URL,
          data: data,
          headers: {
            Authorization: `JWT ${token}`, 
          },
        }
        axios(params)
          .then(()=>{
            const spanText = document.createElement('span')
            spanText.innerText = textboxValue
            parent.childNodes[1].replaceWith(spanText)
            this.updateComment()
        }).catch((e)=>{
          console.log(e)
        })
      }
      else{
        const innerText = parent.childNodes[1].innerText
        parent.childNodes[1].innerText = ''
        const textBox = document.createElement('input')
        textBox.setAttribute('type','text')
        textBox.setAttribute('value', innerText)
        parent.childNodes[1].replaceWith(textBox)
      }
    },
  },
}
</script>

<style>
.total{
  border: 1px solid #aaa;
  border-radius: 30px;
  padding: 20px;
  /* margin-left: 30vh;
  margin-right: 30vh; */
  color: #fff;
}
.title{
  display: flex;
  margin-top: 50px;
  font-size: 50px;
  padding-top: 50px;
}
.mv_score{
  padding-top:20px;
  padding-left:5px;
  font-size:25px;
  content: "★";
  color: gold;
  text-shadow: 0 0 1px #333;
}
.movie_title{
  /* display: flex; */
  text-align: left;
  font-size: 15px;
  margin-left: 5px;
}
.rv_content{
  display: flex;
  font-size: 28px;
  margin-top: 50px;
  margin-bottom: 100px;
  width:100%;
}
.buttons{
  display: flex;
  justify-content : flex-end;
  margin-right: 10px;
  font-size: 25px;
}
.update{
  margin-right:3px;
}
.c-text{
  display: flex;
  margin-bottom:10px;
}
.comment_input{
  margin-top: 40px;
}
.in-line{
  display: flex;
  height: 50px;
}
.detail_input {
    width: 300px;
    height: 39px;
    border-radius:10px;
    background:#FFFFFF;
    outline:none;
    border:none;
    }
.button{
    margin-left:-2.5%;
    height: 40px;
    width: 80px;
    border-radius:10px;
    background: -webkit-linear-gradient(#FF5252, #FF4081);       
    border:none;
}
.comment_total{
  flex-direction: column;
  margin-top:10px;
}
.comment{
  display: flex;
  margin-left: 10px;
  font-size:18px;
}
.comment_update{
  margin-left: 30px;
}
.comment_delete{
  margin-left: 2px;
}
</style>
