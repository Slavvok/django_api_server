<template>
  <div class="home">
  <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Client</a>
        </div>
      </div>
    </nav>
    <div class="container">
    <div class="nomessages"></div>
    <div class="row">
        <div class="col-md-4" v-for="message in messages">
          <p>{{message.date}}</p>
          <p>{{message.text}}</p>
          <time class="timeago" datetime="message.date"></time>
        <p><a class="btn btn-default" role="button" v-on:click="changeState(message)"> Read </a></p>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data: function(){
    return {
      messages: [],
      interval: null,
    }
  },
  created: function(){
    this.getMessages();
    setInterval( function() {
      this.getMessages();
    }.bind(this), 10000);
    this.beforeDestroy();
    this.noMessages(messages);
  },
  methods: {

    getMessages: function() {
      var self = this;
      axios.get('https://slavvok.pythonanywhere.com/api/get_messages/')
      .then(response => {
        self.messages = response.data;
        })
      .catch(error => {
      console.log(error);
      });
  },
    changeState: function(message) {
      var self = this;
      axios.get(`https://slavvok.pythonanywhere.com/api/get_messages/${message.pk}/mark_read/`)
      .then(response => {
        self.message = response.data;
        self.getMessages();
      })
      .catch(error => {
      console.log(error);
      });
    },
  },
    beforeDestroy: function(){
      clearInterval(this.interval);
  },
    noMessages: function(messages){
      if (messages = []){
        return $("#nomessages").html('<h1> No messages. </h1>')
        };
    },
}

</script>

<style>
.navbar-inverse {
    background-color: #99ccff;
    border-color: #080808;
}

.navbar-inverse .navbar-brand {
  color: white;
}

.row {
  margin-top: 10px;
}
.btn-default {
    color: #333;
    background-color: #fff;
    border-color: #ccc;
}

.btn-default:hover{
  background-color: #99ccff;
}

</style>
