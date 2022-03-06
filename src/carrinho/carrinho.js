// <reference types="cypress" />

/* 
  - Estes testes foram feitos utilizando Cypress!
  - Estes testes foram feitos por Ricardo Wagner de Carvalho Lago!
*/

describe('Aba de Carrinho', () => {
  before(() => {
    cy.visit('https://www.kabum.com.br/')
    cy.wait(500)
  })

  //CT_031
  it('Adicionar item “Xbox Series S” ao carrinho', () => {
    cy.visit('https://www.kabum.com.br/produto/128561/console-microsoft-xbox-series-s-512gb-branco-rrs-00006') //Visitando a página do Xbox
    cy.wait(500)

    cy.contains('Console Microsoft Xbox Series S, 512GB, Branco - RRS-00006') //Verificando se esse texto existe nessa página

    // Clicando no botão de Comprar
    cy.get('[id="blocoValores"]').within(() => {
      cy.get('button').contains('COMPRAR').click()
    })

    //Verificando se estou na página de pré-carrinho
    cy.contains('PRODUTO ADICIONADO NO CARRINHO')

    //Clicar no botão ir para o carrinho
    cy.get('[class="buttonGoToCart"]').should('exist').click()
    cy.wait(500)

    //Verificar se está na página de carrinho
    cy.location('href').should('contain', '/carrinho')

    //Voltar para a página inicial
    cy.get('[id="logoKabum"]').click()
  })

  //CT_032
  it('Remover ítem do carrinho', () => {
    /* Adicionar item ao carrinho */
    cy.visit('https://www.kabum.com.br/produto/128561/console-microsoft-xbox-series-s-512gb-branco-rrs-00006') //Visitando a página do Xbox
    cy.wait(500)

    cy.contains('Console Microsoft Xbox Series S, 512GB, Branco - RRS-00006') //Verificando se esse texto existe nessa página

    // Clicando no botão de Comprar
    cy.get('[id="blocoValores"]').within(() => {
      cy.get('button').contains('COMPRAR').click()
    })

    //Verificando se estou na página de pré-carrinho
    cy.contains('PRODUTO ADICIONADO NO CARRINHO')

    //Clicar no botão ir para o carrinho
    cy.get('[class="buttonGoToCart"]').should('exist').click()
    cy.wait(500)

    //Verificar se está na página de carrinho
    cy.location('href').should('contain', '/carrinho')

    //Voltar para a página inicial
    cy.get('[id="logoKabum"]').click()

    /* Adicionar item ao carrinho */

    cy.wait(1000)

    //Cliclar no item de carrinho
    cy.get('[id="linkCarrinhoHeader"]').click()

    //Verificar se está na página de carrinho
    cy.location('href').should('contain', '/carrinho')

    //Removendo ítem do carrinho
    cy.get('[id="buttonRemover"]').click()

    //Verificar se entrou no modal de confirmação
    cy.contains('REMOVER PRODUTO')

    //Cliclar em SIM no modal de confirmação
    cy.get('[id="modalWrapper"]').should('exist').within(() => {
      cy.get('button').contains('SIM').click()
    })

    //Verificar se não existe mais nenhum produto no carrinho
    cy.contains('O seu carrinho está vazio.')

    //Voltar para a home
    cy.get('[id="logoKabum"]').click()
  })

})