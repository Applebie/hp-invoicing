<template>
<header>
    <h1>{{title}}</h1>
    <Button @btn-click="$emit('toggle-add-profile')"  :color="showAddProfile ? 'red':'green'" 
    :text="showAddProfile ? 'Close' : 'AddProfile'" 
    />
    <!-- <Button text="Update Profile" color="blue" /> -->
</header>
</template>
<script>
import Button from './Button.vue'
export default {
    name: 'Header', props:{ title:String,showAddProfile:Boolean},
    components:{Button,},
}
</script>
<style scoped>
header { display: flex; justify-content:space-between;
align-items:center; margin-bottom:20px;}
</style>