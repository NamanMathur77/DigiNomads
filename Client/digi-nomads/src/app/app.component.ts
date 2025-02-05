import { Component } from '@angular/core';
import { CoreService } from './core.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'digi-nomads';

  constructor(private coreService:CoreService){}

  fetchData(){
    this.coreService.greet().subscribe({
      next: (response)=>{
        console.log(response)
      },
      error:(err)=>{
        console.log(err)
      }
    })
  }

  fetchDataFromPromise(){
    this.coreService.fetchDataPromise().then((data)=>{
      console.log(data)
    })
  }
}
