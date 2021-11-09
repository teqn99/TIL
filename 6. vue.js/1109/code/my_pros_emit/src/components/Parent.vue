<template>
<!-- 하나의 컴포넌트 안에는 하나의 태그만!! -> 그래서 div 태그안에 다 묶어두는 것 -->
<div>
  <h1>This is Parent</h1>
  <p>ParentData: {{ parentData }}</p>
  <input v-model="parentData" type="text" @input="inputParentData">
  <p>appData: {{ appData }}</p>
  <p>ChildData: {{ childData }}</p>
  <Child :appData="appData" :parentData="parentData" 
  @child-input="inputChildData"/>
</div>
</template>

<script>
import Child from './Child.vue'

export default {
  name: 'Parent',
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
      // inputChildData가 신호를 받으면, 변수자리(data라 쓰인부분)에 payload(Child에서 보낸 값)이 불러와진다.
      inputChildData: function (data) {
        this.childData = data
        this.$emit('child-input', this.childData)  // 사실 여기 this.childData부분이 payload자리로, 이걸 전송하기 때문에 data에서 받을 수 있는 것
        // console.log('!!!! text from child')
      },
      inputParentData: function () {
        this.$emit('parent-input', this.parentData)
      }
  },
  props: {
    appData: String,
  },
  components: {
      Child,
  },
}
</script>

<style>

</style>