<script lang="ts">
	import type { ReviewIn } from '../interface/ReviewIn.interface';

	export let review: ReviewIn;
</script>

<div class="flex  justify-between  gap-4" id={`${review.id}`}>
	<div class="w-1/3">
		<img src="/books.jpg" alt="" srcset="" class="rounded-full w-24 h-24" />
	</div>
	<div class="w-2/3">
		<h1 class="capitalize font-semibold text-md text-gray-500">
			{review.user.firstname}
			{review.user.lastname}
		</h1>
		<p>{review.comment}</p>
	</div>
</div>
