class SERPParser:

    def extract_domains(self, serp_data):

        domains = []

        for r in serp_data.get("organic_results", []):

            link = r.get("link", "")

            if link:

                domains.append(link.split("/")[2])

        return list(set(domains))