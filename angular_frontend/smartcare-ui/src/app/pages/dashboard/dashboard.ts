import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { Navbar } from '../../components/navbar/navbar';

@Component({
  selector: 'app-dashboard',
  imports: [RouterLink,Navbar],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css',
})
export class Dashboard {
constructor(
    private router: Router
  ) {}

  logout() {

    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');

    this.router.navigate(['/login']);
  }
}
