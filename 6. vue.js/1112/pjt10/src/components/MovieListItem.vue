<template>
  <!-- <div> -->
    <tr>
        <td style="width: 100000px;">
            {{ movie.title }}
        </td>
    </tr>
  <!-- </div> -->
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },

}
</script>

<style>

</style>