<template>
  <form  @submit="onSubmit" class="add-form" >
       <div class="form-control">
      <label>Id </label>
      <input type="text" v-model="id" name="id" />
    </div>
    <div class="form-control">
      <label>Full Name</label>
      <input type="text" v-model="text" name="text" placeholder="John Smith" />
    </div>
    <div class="form-control">
      <label>Business Name</label>
      <input type="text" v-model="business" name="business" placeholder="ABS Ltd." />
    </div>
       <div class="form-control">
      <label>Address</label>
      <input type="text" v-model="address" name="address" placeholder="111 Joe St. NY 11333" />
    </div>
        <div class="form-control">
      <label>Tax Id</label>
      <input type="text" v-model="taxid" name="taxid" placeholder="ID7890900039" />
    </div>

    <input type="submit"  value="Save Task"  class="btn btn-block" />
  </form>
</template>

<script>
export default {
  name: 'AddProfile',
  data() {
    return {
      id: '',  
      text: '',
      business: '',
      address: '',taxid: '',
    }
  },
  methods: {
         
    onSubmit() {
      // e.preventDefault() // if we disable this then DOM wont be refreshed so use getAPI after adding tasks (which has same logic in mount to refresh tasks)

      if (!this.text) {
        alert('Please add a Profile')
        return
      }

      const newProfile = {
        id: this.id,
        text: this.text,
        business: this.business,
        address: this.address,taxid: this.taxid
      }

      this.$emit('add-profile', newProfile)
      this.id = ''
      this.text = ''
      this.business = ''
      this.address = ''
      this.taxid = ''
      
    },
  },
}
</script>

<style scoped>
.add-form {
  margin-bottom: 40px;
}

.form-control {
  margin: 20px 0;
}

.form-control label {
  display: block;
}

.form-control input {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}

.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.form-control-check label {
  flex: 1;
}

.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>

