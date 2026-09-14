<template>
  <section>
    <form class="todo-form" @submit.prevent="addItem">
      <input
        v-model="newTitle"
        type="text"
        placeholder="New task title"
        required
      />
      <button type="submit" :disabled="submitting">Add</button>
    </form>

    <p v-if="error" class="error">{{ error }}</p>
    <p v-if="loading">Loading tasks...</p>

    <ul v-else class="todo-list">
      <li v-for="item in items" :key="item.id">
        <span :class="{ completed: item.completed }">{{ item.title }}</span>
      </li>
      <li v-if="items.length === 0">No tasks yet.</li>
    </ul>
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { API_URL } from '../config'

const items = ref([])
const newTitle = ref('')
const loading = ref(false)
const submitting = ref(false)
const error = ref('')

async function fetchItems() {
  loading.value = true
  error.value = ''
  try {
    const response = await axios.get(`${API_URL}/api/items`)
    items.value = response.data
  } catch (err) {
    error.value = 'Failed to load tasks.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

async function addItem() {
  if (!newTitle.value.trim()) return
  submitting.value = true
  error.value = ''
  try {
    const response = await axios.post(`${API_URL}/api/items`, {
      title: newTitle.value,
      completed: false
    })
    items.value.push(response.data)
    newTitle.value = ''
  } catch (err) {
    error.value = 'Failed to add task.'
    console.error(err)
  } finally {
    submitting.value = false
  }
}

onMounted(fetchItems)
</script>

<style scoped>
.todo-form {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}

.todo-form input {
  flex: 1;
  padding: 8px;
}

.todo-form button {
  padding: 8px 16px;
}

.todo-list {
  list-style: none;
  padding: 0;
}

.todo-list li {
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

.completed {
  text-decoration: line-through;
  color: #888;
}

.error {
  color: red;
}
</style>
