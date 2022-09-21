<script lang="ts">
	import { showModel } from "$root/lib/store/modalStore"
	import { A, Button, CloseButton, Drawer } from "flowbite-svelte"
	let transitionParamsTop = {
		y: -320,
		duration: 200
		// easing: sineIn
	}
</script>

<!-- svelte-ignore missing-declaration -->
<Drawer
	placement="bottom"
	width="w-full"
	transitionType="in:fly"
	transitionParams={transitionParamsTop}
	bind:hidden={$showModel}
>
	<div class="overflow-y-scroll h-screen ">
		<div class="flex items-center">
			<h5
				id="drawer-label"
				class="inline-flex items-center mb-4 text-base font-semibold text-gray-500 dark:text-gray-400"
			>
				<svg
					class="mr-2 w-5 h-5"
					aria-hidden="true"
					fill="currentColor"
					viewBox="0 0 20 20"
					xmlns="http://www.w3.org/2000/svg"
					><path
						fill-rule="evenodd"
						d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
						clip-rule="evenodd"
					/></svg
				>Top drawer
			</h5>
			<CloseButton
				on:click={() => ($showModel = true)}
				class="mb-4 dark:text-white"
			/>
		</div>
		<p class="max-w-lg mb-6 text-sm text-gray-500 dark:text-gray-400">
			Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto nostrum,
			maiores porro cupiditate doloribus est quas iure vitae, eius atque, at hic
			quibusdam facere ullam. Natus soluta necessitatibus molestiae officiis
			incidunt dolores ut minus veniam voluptatum sint tempora eius quas saepe
			dolor pariatur ipsam, cum dicta molestias, dignissimos blanditiis facilis
			iusto, sit doloribus similique. Earum corrupti soluta aliquam veritatis
			quasi recusandae ullam obcaecati aperiam dolore ipsam illo blanditiis
			voluptatibus veniam, dolorum sequi eligendi natus. Vel voluptatum
			explicabo maxime consequuntur qui architecto maiores quasi optio animi
			laudantium, eligendi nesciunt placeat eum doloribus quae fuga illum,
			veniam labore adipisci magni? Optio accusantium temporibus consectetur
			doloribus debitis? Autem, tenetur quia impedit at soluta maiores qui harum
			sapiente quasi tempore consectetur. Repudiandae molestias sit aliquid odio
			numquam totam fugit voluptatum ratione, corrupti consequuntur, quo saepe
			recusandae! Praesentium eos minus facere quis veritatis eaque alias
			temporibus assumenda delectus recusandae. Ut consequuntur facilis pariatur
			ullam doloribus aspernatur voluptatum fugiat placeat repellendus molestias
			reprehenderit fugit, aliquam eos nostrum eum beatae odit accusantium
			sapiente. Dolore accusantium eius provident cum quo possimus autem nemo
			beatae. Qui culpa, veritatis impedit, cumque doloremque modi magnam
			sapiente eligendi fuga natus nulla corrupti aliquam incidunt excepturi
			repellat, ducimus consequuntur aliquid officia repellendus rerum vero?
			Iusto nesciunt, reiciendis blanditiis repellat cumque in at iste, atque
			libero quisquam, laborum porro nam similique assumenda impedit natus!
			Praesentium quasi minus dolore repudiandae culpa autem labore. Maiores ad
			sunt reprehenderit perspiciatis non magni, ullam dolorum illo eligendi
			inventore impedit, deleniti beatae! Obcaecati sequi perspiciatis, atque,
			cumque doloribus alias nobis error facere aperiam dolore neque voluptatum
			consequuntur! Tempore ea eligendi dolores! Reiciendis architecto aut
			veniam doloribus iste ab? Dolorum ex quod consequuntur, incidunt,
			laboriosam labore praesentium non, corporis et quos nesciunt recusandae
			reprehenderit deserunt? Perspiciatis accusantium magni aspernatur saepe
			sapiente nostrum illo eligendi aliquam ducimus magnam totam ex eveniet
			obcaecati velit expedita dolores iure autem, voluptate corporis quae
			repudiandae vel. Quo unde odio ullam exercitationem illum nesciunt tempora
			accusantium sit sint, magnam, repellendus aliquid libero dicta reiciendis,
			recusandae excepturi nihil laboriosam itaque nam numquam et! Velit ea,
			vitae repellat, voluptatibus, voluptatem ipsum suscipit beatae numquam
			esse nihil facilis aliquid dicta non quis illum cumque laborum amet
			voluptate nisi maxime? Quae aperiam expedita tenetur quo eligendi eveniet
			assumenda illo impedit quas vel. Maxime at vero assumenda, ipsam quidem
			eius cumque voluptas eaque sit. Quaerat quam cumque, provident sit harum
			vel facilis praesentium eveniet nostrum, quas modi amet fugit officia eius
			aspernatur reiciendis porro numquam nihil deserunt vitae in neque sint
			labore. Porro culpa at minima modi labore unde esse repellendus voluptatem
			sequi cumque! Libero beatae voluptates a nesciunt illo sint, aperiam
			provident atque sunt ratione culpa incidunt numquam reiciendis obcaecati
			asperiores consequatur blanditiis vero distinctio dolores cum doloribus
			animi fugiat. Temporibus quod sed modi minus molestias nisi veniam rerum
			ea rem dolor magnam, itaque, deserunt culpa delectus aspernatur dolores
			distinctio, neque totam debitis ab unde! Molestias voluptatibus laborum
			nisi recusandae consectetur quas beatae corporis iusto sunt blanditiis id
			perferendis, possimus suscipit impedit, similique facere obcaecati. Neque
			sunt pariatur vitae cum? Lorem ipsum dolor sit amet consectetur,
			adipisicing elit. Quam alias omnis quos cumque exercitationem hic
			recusandae vel voluptatum. Obcaecati nesciunt aspernatur saepe rem
			eligendi earum dolore sunt impedit nam ea blanditiis voluptas, aliquid
			voluptatibus, unde, non provident! Quas quod in sit et esse fugiat
			blanditiis doloremque dolores magnam consectetur soluta nesciunt rerum
			saepe nostrum repudiandae, excepturi molestiae accusamus numquam
			architecto, beatae fugit dolore. Aliquid fugit explicabo quidem nemo iure,
			aut corporis omnis, illum, eum vel ipsum qui molestiae provident amet
			quisquam. Sequi eius et aperiam dicta, sint commodi! Quaerat nulla eum
			error modi alias corporis asperiores temporibus facere placeat nihil
			libero optio, nesciunt fugiat recusandae ab? Dolore nesciunt, tempora
			eaque aperiam placeat magnam earum quidem unde officiis rerum deserunt
			soluta. Molestiae porro eius eos ad dolore? Repudiandae eligendi nostrum
			quasi adipisci enim mollitia sit praesentium tenetur, tempore laudantium
			veritatis illum repellendus reprehenderit magni consequatur quaerat minus
			blanditiis est voluptates quod. Deleniti odit alias dignissimos aspernatur
			dolores corporis
		</p>
		<Button color="light" href="/">Learn more</Button>
		<Button href="/" class="ml-2"
			>Get access <svg
				class="w-4 h-4 ml-1"
				aria-hidden="true"
				fill="currentColor"
				viewBox="0 0 20 20"
				xmlns="http://www.w3.org/2000/svg"
				><path
					fill-rule="evenodd"
					d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
					clip-rule="evenodd"
				/></svg
			></Button
		>
	</div>
</Drawer>
