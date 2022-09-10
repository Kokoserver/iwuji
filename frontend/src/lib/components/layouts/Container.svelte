<script lang="ts">
	export let divClass: string = ""
</script>

<div class={`container mx-auto  ${divClass}`}>
	<slot />
</div>
