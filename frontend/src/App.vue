<template>
  <router-view />
</template>
<script setup>
import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/components/Dashboard.vue'
const routes = [{ path: '/', component: Dashboard }]
const router = createRouter({ history: createWebHistory(), routes })
</script>
