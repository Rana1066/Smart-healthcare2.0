import { Component } from '@angular/core';
import { Navbar } from '../../components/navbar/navbar';
import { CommonModule } from '@angular/common';
import {  BillingServices } from '../../services/billing';

@Component({
  selector: 'app-billing',
  imports: [CommonModule,Navbar],
  templateUrl: './billing.html',
  styleUrl: './billing.css',
})
export class Billing {
 bills: any[] = [];

  constructor(
    private billingService: BillingServices
  ) {}

  ngOnInit(): void {
    this.loadBills();
  }

  loadBills() {

    this.billingService
      .getBills()
      .subscribe({
        next: (data: any) => {
          this.bills = data;
        },
        error: (error: any) => {
          console.log(error);
        }
      });
  }
}
