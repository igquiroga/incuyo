

<?php 
if(empty($marca) and empty($id)){
	echo '
	<div class="card" style="width: 18rem;">
	<div class="card-body">
		<h5 class="card-title">Card title</h5>
		<p class="card-text">Some quick example text to build on the card title and make up the bulk of the cards content.</p>
		<a href="#" class="btn btn-primary">Go somewhere</a>
		</div>
	</div>
	';
}
if(!(empty($marca))){
	echo '<p>Marca: '.$marca.'</p>';
} 
if(!(empty($id))){
	echo '<p>Id: '.$id.'</p>';
}
?>
