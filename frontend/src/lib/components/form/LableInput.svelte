<script lang="ts">
	import { Helper, Input, Label } from 'flowbite-svelte';
	export let value: string;
	export let handleChange: (event: Event) => void;
	export let name: string;
	export let placeholder: string;
	export let required: boolean = true;
	export let custom_error: string = '';
	export let labeleValue: string;
	export let showLable: boolean = true;
	export let type:
		| 'color'
		| 'date'
		| 'datetime-local'
		| 'email'
		| 'file'
		| 'hidden'
		| 'image'
		| 'month'
		| 'number'
		| 'password'
		| 'reset'
		| 'submit'
		| 'tel'
		| 'text'
		| 'time'
		| 'url'
		| 'week';
	export let error: string;
</script>

<Label class="space-y-2" show={showLable}>
	<span>{labeleValue}</span>
	<Input {type} bind:value on:change={handleChange} {name} {placeholder} {required} />
	{#if error}
		<Helper color="red">{error ?? custom_error}</Helper>
	{/if}
</Label>
