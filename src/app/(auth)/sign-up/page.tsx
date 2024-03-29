import UserAuthForm from "../_components/UserAuthForm";
import { SVGLineGlowAnimateContainer } from "../_components/LineGlowAnimation";
import type { Metadata } from "next";

import { BarChart4 } from "lucide-react";

export const metadata: Metadata = {
  title: "Create account",
};

export default function SignupPage() {
  return (
    <>
      <div className="w-full flex overflow-hidden">
        <section className="px-4 py-12 mx-auto max-w-lg mt-28 md:max-w-xl lg:max-w-7xl sm:px-16 md:px-12 lg:px-24 lg:py-24">
          <div className="justify-center bg-stone-300 dark:bg-stone-900 mx-auto text-left align-bottom transition-all transform group rounded-xl sm:align-middle ">
            <div className="grid flex-wrap items-center justify-center grid-cols-1 mx-auto shadow-sm group-hover:shadow-lg transition-shadow lg:grid-cols-2 rounded-xl">
              <div className="px-6 py-3 ">
                <div className="flex flex-col space-y-2 text-center mb-6 mt-4">
                  <BarChart4 className="mx-auto h-10 w-10" />
                  <h1 className="text-2xl font-semibold tracking-tight">
                    Register
                  </h1>
                </div>
                <UserAuthForm isSignup={true}/>
              </div>
              <div className="order-first hidden w-full lg:flex justify-center">
                <SVGLineGlowAnimateContainer />
              </div>
            </div>
          </div>
        </section>
      </div>
    </>
  );
}
