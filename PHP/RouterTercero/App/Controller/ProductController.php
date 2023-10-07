<?php 
namespace App\Controller;

class ProductController extends Controller{

	public function productos($view, $marca="", $id=""){
		return $this->view($view);
	}
	
}


?>