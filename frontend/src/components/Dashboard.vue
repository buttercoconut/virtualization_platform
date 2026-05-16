<template>
  <div>
    <h2>Dashboard</h2>
    <vm-list></vm-list>
    <vm-form></vm-form>
  </div>
</template>
<script setup>
import VMList from '@/components/VMList.vue'
import VMForm from '@/components/VMForm.vue'

export default {
  components: { VMList, VMForm }
}
</script>
