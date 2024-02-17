import { Button, Link } from "@nextui-org/react";

// import { sectionWrapper } from "@/components/primitives";
// import { RelumeLogo, Story2DesignLogo } from "@/components/icons/sponsors";
import { Airplay } from "lucide-react";
// import { VercelIcon } from "@/components/icons/social";
// import { siteConfig } from "@/config/site";

type Sponsor = {
  name: string;
  href: string;
  logo: React.ReactNode;
};
const sponsors: Sponsor[] = [
  {
    name: "Relume",
    href: "https://library.relume.io/ai-site-builder?via=nextui",
    logo: <Airplay className="text-black dark:text-white" />,
  },
  {
    name: "story.to.design",
    href: "https://story.to.design?utm_source=nextui&utm_marketing=partnership",
    logo: <Airplay className="pt-1" />,
  },
  {
    name: "Vercel",
    href: "https://www.vercel.com?utm_source=nextui&utm_marketing=oss",
    logo: <Airplay className="text-black dark:text-white" height={24} />,
  },
];

export const Sponsors = () => {
  return (
    <section
    //   className={sectionWrapper({ class: "text-center mt-24 lg:mt-32" })}
    >
      <h3 className="text-large text-default-500">Supported and backed by</h3>
      <div className="w-full flex flex-wrap gap-x-5 gap-y-3 justify-center items-center">
        {sponsors.map((sponsor) => {
          return sponsor.logo;
        })}
        <Button
          isExternal
          as={Link}
          className="group text-sm border-dashed font-normal text-default-600 data-[hover=true]:bg-default-100/50"
          //   href={siteConfig.links.sponsor}
          startContent={
            <Airplay className="text-danger group-data-[hover=true]:animate-heartbeat" />
          }
          variant="bordered"
        >
          Your Company
        </Button>
      </div>
    </section>
  );
};
