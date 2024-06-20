<template>
    <div class="welcome">
      <h1>Welcome to Your Mortgage Calculator</h1>
      <div class="buttons">
        <button class="large-button" @click="navigate('purchasing')">Purchasing</button>
        <button class="large-button" @click="navigate('refinancing')">Refinancing</button>
        <button class="large-button" @click="navigate('renewing')">Renewing</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Welcome',
    methods: {
      navigate(page) {
        if (page === 'refinancing') {
          this.$router.push({ name: 'Refinancing' });
        }
      }
    }
  };
  </script>
  
  <style>
  .welcome {
    text-align: center;
  }
  .buttons {
    display: flex;
    justify-content: center;
    gap: 10px;
  }
  .large-button {
    background-color: blue;
    color: white;
    padding: 20px;
    font-size: 20px;
    border: none;
    cursor: pointer;
  }
  .large-button:hover {
    background-color: darkblue;
  }
  </style>
  