<template>
  <main class="container">
    <h1>Todo App</h1>
    <TodoList />
  </main>
</template>

<script setup>
import TodoList from './components/TodoList.vue'
</script>

<style>
.container {
  max-width: 480px;
  margin: 40px auto;
  font-family: Arial, Helvetica, sans-serif;
  padding: 0 16px;
}
</style>
