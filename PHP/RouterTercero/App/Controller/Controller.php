<?php 
namespace App\Controller;

class Controller{

	public function view($view){
		ob_start();
		require_once($view);
		$content = ob_get_clean();
		return $content;
	}

	
}


?>