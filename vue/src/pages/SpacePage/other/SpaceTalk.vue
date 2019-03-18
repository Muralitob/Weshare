<template>
  <div>
    <div class="talk">
      <div class="talk_board">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos totam voluptatibus fugiat corporis repellat facilis aliquid nobis, vero dolor voluptatem. Incidunt excepturi rerum vel explicabo iure, alias laboriosam quaerat. Cumque.
      </div>
      <div class="input">
        <textarea class="talk_input">
        </textarea>
          <button class="talk_send">发送</button>
      </div>
    </div>
      <div class="info">

      </div>

  </div>

</template>

<script>
export default {
  data() {
    return {
      line: [
        
      ]
    }
  }
}
</script>

<style lang="scss">
  .talk {
    width: 100%;
    height: 100%;
    &_board {
      width: 100%;
      height: 520px;
      background-color: #eee;
      overflow: auto;
      padding: 20px;
      &::-webkit-scrollbar {
        display: none;
      }
    }
    &_input {
      border: none;
      border-top: 1px solid #ccc;
      height: 120px;
      background-color: #eee;
      position: relative;
      width: 100%;
      resize: none;
      outline: none;
      &:focus {
        background-color: #fff;
      }
    }
    &_send {
      float: right;
      position: relative;
      top: -60px;
      left: -20px;
      background-color: #eee;
      width: 120px;
      height: 42px;
      // outline: none;
      border: 1px solid #ccc;
      &:hover {
        background-color: #01d277;
        color: #fff;
      }
    }
  }
  .input {
    background-color: #eee;
    &:focus {
      background-color: #fff;
    }

  }
</style>
