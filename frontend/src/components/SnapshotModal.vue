<template>
  <div class="snapshot-modal">
    <h3>Create Snapshot</h3>
    <form @submit.prevent="createSnapshot">
      <label>Name: <input v-model="name" required /></label>
      <div class="actions">
        <button type="submit">Create</button>
        <button type="button" @click="close">Cancel</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const emit = defineEmits(['created', 'close']);
const name = ref('');

const createSnapshot = async () => {
  try {
    await axios.post('/api/snapshots', {
      name: name.value,
    });
    emit('created');
    close();
  } catch (e) {
    console.error('Create snapshot failed', e);
  }
};

const close = () => {
  emit('close');
};
</script>

<style scoped>
.snapshot-modal {
  border: 1px solid #ccc;
  padding: 15px;
  margin-top: 15px;
}
.snapshot-modal label {
  display: block;
  margin-bottom: 8px;
}
.snapshot-modal .actions {
  margin-top: 10px;
}
.snapshot-modal button {
  margin-right: 5px;
}
</style>